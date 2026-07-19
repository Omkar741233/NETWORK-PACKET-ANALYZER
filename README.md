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
## ⚙️ How It Works

The Network Packet Analyzer captures and analyzes live network traffic using either **raw sockets** or the **Scapy** library. It listens on a specified network interface (or automatically selects one), processes each captured packet, extracts key networking information, and displays the results in a readable format.

### Workflow

1. **Start the Program**
   - The user runs the application from the command line and specifies the number of packets to capture and, optionally, the network interface.

2. **Initialize Packet Capture**
   - The program checks whether Scapy should be used. If not, it captures packets using raw sockets.

3. **Listen for Network Traffic**
   - The analyzer continuously listens for incoming and outgoing packets on the selected network interface.

4. **Capture Packets**
   - Each packet is intercepted in real time before being processed.

5. **Analyze Packet Headers**
   - The program extracts important information from the packet, including:
     - Source IP Address
     - Destination IP Address
     - Protocol (TCP, UDP, ICMP, etc.)
     - Source and Destination Ports (when applicable)
     - Packet Payload
     - Additional protocol-specific details

6. **Display Packet Information**
   - The extracted information is formatted and displayed in the terminal, making it easy to understand the captured network traffic.

7. **Stop After Capturing the Requested Number of Packets**
   - Once the specified packet count is reached, the program exits gracefully.

---

## 🔄 Working Flow

```
User Starts Program
        │
        ▼
Select Network Interface
        │
        ▼
Initialize Raw Socket / Scapy
        │
        ▼
Capture Live Network Packets
        │
        ▼
Extract Packet Headers
(IP, TCP, UDP, ICMP)
        │
        ▼
Analyze Packet Information
        │
        ▼
Display Packet Details
        │
        ▼
Repeat Until Packet Count is Reached
        │
        ▼
Program Ends
```


---
## 📚 Concepts Used

This project is based on the following networking and cybersecurity concepts:

- **Computer Networks**
- **Packet Sniffing**
- **Network Packet Analysis**
- **Raw Socket Programming**
- **Scapy Library**
- **IP (Internet Protocol)**
- **TCP (Transmission Control Protocol)**
- **UDP (User Datagram Protocol)**
- **ICMP (Internet Control Message Protocol)**
- **Packet Header Parsing**
- **Source and Destination IP Address Analysis**
- **Port Number Analysis**
- **Hexadecimal Data Representation (Hex Dump)**
- **Command-Line Interface (CLI)**
- **Network Interface Selection**
- **Real-Time Packet Capture**
- **Exception Handling**
- **Cross-Platform Programming (Windows, Linux, macOS)**
- **Python Programming**


---
## 🚀 Future Improvements

The following features can be added in future versions of this project:

- Add a Graphical User Interface (GUI) using Tkinter or PyQt.
- Save captured packets to **PCAP** files for analysis in Wireshark.
- Export packet details to **CSV**, **JSON**, or **PDF** reports.
- Implement protocol-based packet filtering (TCP, UDP, ICMP, HTTP, DNS, etc.).
- Add IP address geolocation and hostname resolution.
- Display real-time network traffic statistics and protocol usage.
- Detect suspicious or malicious network activity.
- Add support for IPv6 packet analysis.
- Improve packet payload inspection with detailed protocol decoding.
- Introduce multi-threading for better performance during high network traffic.
- Create a web-based dashboard for remote monitoring.
- Add logging functionality to maintain packet capture history.
- Support packet capture on multiple network interfaces simultaneously.
- Implement customizable capture filters and search functionality.
- Add graphical charts for bandwidth and traffic analysis.


---

## ⚠️ Disclaimer

This project is developed **solely for educational and research purposes** to help users understand the fundamentals of network packet analysis and cybersecurity.

Users are responsible for ensuring they have **proper authorization** before capturing or analyzing network traffic. Unauthorized packet sniffing or monitoring on networks you do not own or have permission to access may violate privacy laws, organizational policies, or local regulations.

The author is **not responsible** for any misuse, unauthorized activities, or damages resulting from the use of this software. Always use this tool ethically, responsibly, and in compliance with applicable laws.
---
## 🤝 Contributing

Contributions are welcome! If you would like to improve this project, please follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit them.
   ```bash
   git commit -m "Add your meaningful commit message"
   ```
4. Push your branch to your fork.
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request (PR) describing your changes.

### Contribution Guidelines

- Follow the existing code style and project structure.
- Write clear, meaningful commit messages.
- Test your changes before submitting.
- Update the documentation (`README.md`) if your changes affect usage or functionality.
- Be respectful and constructive during code reviews.

Thank you for helping improve this project! 🚀


---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Omkar Ghadge**

Cybersecurity Enthusiast | Diploma Student

GitHub:
https://github.com/Omkar741233

LinkedIn:
https://www.linkedin.com/in/YOUR_LINKEDIN_PROFILE/

---

## ⭐ Support

If you find this project useful, consider supporting it by:

- ⭐ Starring this repository on GitHub.
- 🍴 Forking the repository to contribute or build upon it.
- 🐛 Reporting bugs by opening an Issue.
- 💡 Suggesting new features or improvements.
- 📢 Sharing the project with others who are interested in networking and cybersecurity.

Your support and feedback help improve this project and encourage future development.

Thank you for your support! 🚀
