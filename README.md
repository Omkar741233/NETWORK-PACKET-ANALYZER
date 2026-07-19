# NETWORK-PACKET-ANALYZER

# 🔍 Network Packet Analyzer

A Python-based **Network Packet Analyzer** that captures and analyzes live network traffic. This tool displays packet information such as source IP, destination IP, protocol, packet length, and other useful details to help users understand network communication and basic packet analysis.

---

## 📖 About the Project

The Network Packet Analyzer is designed for students and beginners in cybersecurity who want to learn how network packets travel across a network. It captures live packets from a selected network interface and presents packet details in a simple, readable format.

This project demonstrates the basics of packet sniffing using Python and Scapy and can be used as a learning tool for networking and ethical hacking.

---

## ✨ Features

- Capture live network packets
- Display Source IP and Destination IP
- Identify network protocols (TCP, UDP, ICMP, etc.)
- Show packet length and packet summary
- Real-time packet monitoring
- Simple command-line interface
- Lightweight and beginner-friendly

---

## 🛠 Technologies Used

- Python 3
- Scapy
- Kali Linux
- Linux Networking

---

## 📂 Project Structure

```
Network-Packet-Analyzer/
│
├── main.py
├── requirements.txt
├── README.md
├── screenshots/
│   ├── output1.png
│   ├── output2.png
│
└── LICENSE
```

---

## 📋 Requirements

- Python 3.x
- Kali Linux (Recommended)
- Root/Sudo privileges
- Scapy Library

---

## ⚙ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Network-Packet-Analyzer.git
```

### 2. Move to the project directory

```bash
cd Network-Packet-Analyzer
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install scapy
```

---

## ▶ Running the Project

Run the program with administrator privileges.

```bash
sudo python3 main.py
```

---

## 🖥 Example Output

```
Packet Captured

Source IP      : 192.168.1.15
Destination IP : 142.250.183.78
Protocol       : TCP
Length         : 60 Bytes

----------------------------------------
```

---

## 📷 Screenshots

Add screenshots inside the **screenshots** folder.

Example:

```
screenshots/output1.png
screenshots/output2.png
```

Display them in README:

```md
## Screenshots

![Output 1](screenshots/output1.png)

![Output 2](screenshots/output2.png)
```

---

## 🧠 How It Works

1. Starts listening on the selected network interface.
2. Captures packets in real time.
3. Extracts important packet information.
4. Identifies the protocol.
5. Displays packet details in the terminal.

---

## 📚 Concepts Used

- Packet Sniffing
- IP Header Analysis
- TCP
- UDP
- ICMP
- Network Interfaces
- Packet Parsing
- Cybersecurity Basics

---

## 🎯 Future Improvements

- Graphical User Interface (GUI)
- Save packets to PCAP files
- Export captured data to CSV
- Protocol statistics
- Packet filtering
- DNS packet analysis
- HTTP packet inspection
- Network traffic visualization

---

## ⚠ Disclaimer

This project is created **only for educational and ethical purposes**. Use it only on networks that you own or have permission to monitor.

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Omkar Ghadge**

Cybersecurity Enthusiast | Diploma Student

GitHub:
https://github.com/YOUR_USERNAME

LinkedIn:
https://www.linkedin.com/in/YOUR_LINKEDIN_PROFILE/

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
