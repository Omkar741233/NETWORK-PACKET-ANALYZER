import argparse
import os
import platform
import socket
import struct
import sys
import textwrap

try:
    from scapy.all import sniff, IP, TCP, UDP, ICMP
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False


def hexdump(data, length=16):
    lines = []
    for i in range(0, len(data), length):
        chunk = data[i : i + length]
        hex_bytes = " ".join(f"{b:02x}" for b in chunk)
        text = "".join((chr(b) if 32 <= b < 127 else ".") for b in chunk)
        lines.append(f"{i:04x}  {hex_bytes:<{length*3}}  {text}")
    return "\n".join(lines)


def parse_ip_header(packet):
    if len(packet) < 20:
        return None
    version_ihl = packet[0]
    version = version_ihl >> 4
    ihl = (version_ihl & 0xF) * 4
    protocol = packet[9]
    src_ip = socket.inet_ntoa(packet[12:16])
    dst_ip = socket.inet_ntoa(packet[16:20])
    return {
        "version": version,
        "ihl": ihl,
        "protocol": protocol,
        "src_ip": src_ip,
        "dst_ip": dst_ip,
        "header_length": ihl,
        "payload": packet[ihl:],
    }


def parse_tcp_header(payload):
    if len(payload) < 20:
        return None
    src_port, dst_port, seq, ack, offset_reserved_flags = struct.unpack("!HHLLH", payload[:14])
    data_offset = (offset_reserved_flags >> 12) * 4
    flags = offset_reserved_flags & 0x01FF
    return {
        "src_port": src_port,
        "dst_port": dst_port,
        "sequence": seq,
        "acknowledgement": ack,
        "header_length": data_offset,
        "flags": flags,
        "payload": payload[data_offset:],
    }


def parse_udp_header(payload):
    if len(payload) < 8:
        return None
    src_port, dst_port, length = struct.unpack("!HHH", payload[:6])
    return {
        "src_port": src_port,
        "dst_port": dst_port,
        "length": length,
        "payload": payload[8:],
    }


def parse_icmp_header(payload):
    if len(payload) < 4:
        return None
    icmp_type, code, checksum = struct.unpack("!BBH", payload[:4])
    return {
        "type": icmp_type,
        "code": code,
        "checksum": checksum,
        "payload": payload[4:],
    }


def format_packet_summary(index, info):
    lines = [f"Packet {index}", "=========="]
    lines.append(f"Source:      {info['src_ip']}" + (f":{info['src_port']}" if info.get('src_port') else ""))
    lines.append(f"Destination: {info['dst_ip']}" + (f":{info['dst_port']}" if info.get('dst_port') else ""))
    lines.append(f"Protocol:    {info['protocol_name']} ({info['protocol']})")
    if info.get('extra'):
        lines.append(f"Details:     {info['extra']}")
    lines.append(f"Payload:     {len(info['payload'])} bytes")
    lines.append("Data:        \n" + hexdump(info['payload'][:128]))
    return "\n".join(lines)


def capture_with_socket(interface, count):
    system = platform.system().lower()
    if system == "windows":
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        sock.bind((interface, 0))
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    else:
        sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        sock.bind((interface, 0))

    packet_index = 0
    try:
        while packet_index < count:
            raw_data, addr = sock.recvfrom(65535)
            if system != "windows":
                if len(raw_data) < 14:
                    continue
                eth_proto = struct.unpack("!H", raw_data[12:14])[0]
                if eth_proto != 0x0800:
                    continue
                ip_header_data = raw_data[14:]
            else:
                ip_header_data = raw_data

            ip_info = parse_ip_header(ip_header_data)
            if not ip_info:
                continue

            packet_index += 1
            info = {
                "src_ip": ip_info["src_ip"],
                "dst_ip": ip_info["dst_ip"],
                "protocol": ip_info["protocol"],
                "payload": ip_info["payload"],
                "extra": "",
            }
            proto = ip_info["protocol"]
            if proto == 6:
                tcp = parse_tcp_header(ip_info["payload"])
                info["protocol_name"] = "TCP"
                if tcp:
                    info.update({
                        "src_port": tcp["src_port"],
                        "dst_port": tcp["dst_port"],
                        "payload": tcp["payload"],
                        "extra": f"seq={tcp['sequence']} ack={tcp['acknowledgement']} flags={tcp['flags']:03b}",
                    })
            elif proto == 17:
                udp = parse_udp_header(ip_info["payload"])
                info["protocol_name"] = "UDP"
                if udp:
                    info.update({
                        "src_port": udp["src_port"],
                        "dst_port": udp["dst_port"],
                        "payload": udp["payload"],
                        "extra": f"length={udp['length']}",
                    })
            elif proto == 1:
                icmp = parse_icmp_header(ip_info["payload"])
                info["protocol_name"] = "ICMP"
                if icmp:
                    info.update({
                        "payload": icmp["payload"],
                        "extra": f"type={icmp['type']} code={icmp['code']}",
                    })
            else:
                info["protocol_name"] = f"IP protocol {proto}"

            print(format_packet_summary(packet_index, info))
            print()
    finally:
        if system == "windows":
            try:
                sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
            except OSError:
                pass
        sock.close()


def capture_with_scapy(interface, count):
    def callback(packet):
        nonlocal packet_index
        packet_index += 1
        info = {
            "src_ip": packet[IP].src,
            "dst_ip": packet[IP].dst,
            "protocol": packet[IP].proto,
            "protocol_name": packet[IP].proto,
                "payload": bytes(packet[IP].payload.payload) if packet[IP].payload else b"",
                "extra": "",
        }

        if packet.haslayer(TCP):
            tcp = packet[TCP]
            info.update({
                "protocol_name": "TCP",
                "src_port": tcp.sport,
                "dst_port": tcp.dport,
                "payload": bytes(tcp.payload),
                "extra": f"seq={tcp.seq} ack={tcp.ack} flags={tcp.flags}",
            })
        elif packet.haslayer(UDP):
            udp = packet[UDP]
            info.update({
                "protocol_name": "UDP",
                "src_port": udp.sport,
                "dst_port": udp.dport,
                "payload": bytes(udp.payload),
                "extra": f"length={udp.len}",
            })
        elif packet.haslayer(ICMP):
            icmp = packet[ICMP]
            info.update({
                "protocol_name": "ICMP",
                "payload": bytes(icmp.payload),
                "extra": f"type={icmp.type} code={icmp.code}",
            })
        else:
            info["protocol_name"] = f"IP protocol {packet[IP].proto}"

        print(format_packet_summary(packet_index, info))
        print()

        if packet_index >= count:
            raise KeyboardInterrupt

    packet_index = 0
    sniff(iface=interface, prn=callback, store=False)


def choose_interface(provided_iface):
    if provided_iface:
        return provided_iface
    if platform.system().lower() == "windows":
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    return "eth0"


def main():
    parser = argparse.ArgumentParser(description="Python Network Packet Analyzer")
    parser.add_argument("-i", "--interface", help="Network interface or IP address to listen on")
    parser.add_argument("-c", "--count", type=int, default=10, help="Number of packets to capture")
    parser.add_argument("--use-scapy", action="store_true", help="Use Scapy for packet capture if installed")
    args = parser.parse_args()

    interface = choose_interface(args.interface)
    if args.use_scapy and not SCAPY_AVAILABLE:
        print("Scapy is not installed. Falling back to raw socket capture.")
        args.use_scapy = False

    print(f"Listening on {interface} ({'Scapy' if args.use_scapy else 'raw socket'}) for {args.count} packet(s)...\n")
    try:
        if args.use_scapy:
            capture_with_scapy(interface, args.count)
        else:
            capture_with_socket(interface, args.count)
    except KeyboardInterrupt:
        print("\nCapture stopped by user.")
    except PermissionError:
        print("Permission denied. Run this script with administrator/root privileges.")
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
