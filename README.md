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
## 🛠️ Technologies Used

- **Python 3** – Core programming language used to develop the application.
- **Scapy** – Python library for packet sniffing, packet manipulation, and network analysis.
- **Kali Linux** – Operating system used for development and testing.
- **Linux Networking** – Used for capturing and analyzing network traffic.
- **Command Line Interface (CLI)** – User interface for running the application and viewing packet information.
- **Git** – Version control system for tracking changes.
- **GitHub** – Repository hosting and project collaboration platform.
---



```
## 📂 Project Structure

Network-Packet-Analyzer/
│
├── main.py                 # Main program file
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── LICENSE                 # MIT License
├── screenshots/            # Project screenshots
│   ├── output1.png
│   └── output2.png
├── output/                 # Saved output files (optional)
└── .gitignore              # Files ignored by Git

```

---

## 📋 Requirements

Before running this project, ensure you have the following installed:

- **Python 3.8 or later**
- **Scapy** (`pip install scapy`)
- **Npcap** (Windows only, if running on Windows)
- **Kali Linux** or any Linux distribution (recommended)
- **Root/Sudo privileges** (required for live packet capture)
- **Git** (optional, for cloning the repository)


---
## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Omkar741233/NETWORK-PACKET-ANALYZER.git
cd NETWORK-PACKET-ANALYZER
```

---

# 🐧 Linux (Kali Linux, Ubuntu, Debian)

### Step 1: Update the system

```bash
sudo apt update
```

### Step 2: Install Python and pip

```bash
sudo apt install python3 python3-pip -y
```

### Step 3: Install Scapy (Optional)

```bash
pip3 install scapy
```

### Step 4: Run the program

Using raw sockets:

```bash
sudo python3 packet_analyzer.py -i eth0 -c 10
```
> you can change the numbers of packets you see '10' it is a number of packets

Using Scapy:

```bash
sudo python3 packet_analyzer.py -i eth0 -c 10 --use-scapy
```

> Replace `eth0` with your network interface (for example, `wlan0` or `ens33`).

---


---


## 🪟 Windows Installation

### Step 1: Clone the Repository

```cmd
git clone https://github.com/Omkar741233/NETWORK-PACKET-ANALYZER.git
cd NETWORK-PACKET-ANALYZER
```
### Step 2: Install Python

Download and install **Python 3.x** from:
https://www.python.org/downloads/

### Step 3: Install Npcap

Download and install **Npcap** from:
https://npcap.com/

### Step 4: Install Scapy (Optional)

```cmd
pip install scapy
```

### Step 5: Navigate to the Project Directory

```cmd
cd C:\Users\USER\network
```

### Step 6: Run the Program

Using raw socket capture:

```cmd
python packet_analyzer.py -c 5
```

Capture 20 packets:

```cmd
python packet_analyzer.py -c 20
```

Using Scapy:

```cmd
python packet_analyzer.py -c 5 --use-scapy
```

Specify a local IP address:

```cmd
python packet_analyzer.py -i YOUR_IP_ADDRESS -c 5
```

...


## ⚠ Notes

- Run the program with **Administrator** (Windows) or **Root/Sudo** (Linux/macOS) privileges.
- Ensure the correct network interface or IP address is specified.
- Scapy is optional. If it is not installed, the program automatically falls back to raw socket packet capture.
- Packet capturing may require additional permissions depending on your operating system.
```
```
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
