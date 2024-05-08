# PRODIGY_CS_05
Network Packet Analyzer
# Network Packet Analyzer

This is a simple packet sniffer tool developed in Python using the `scapy` library. The tool captures and analyzes network packets, displaying relevant information such as source and destination IP addresses, protocols, and payload data. It is designed for educational purposes to help users understand how network packets are structured and transmitted over a network.

## Features

- Captures network packets in real-time.
- Analyzes captured packets to extract source and destination IP addresses, protocol types (TCP or UDP), and payload data.
- Prints the extracted information in a user-friendly format for easy analysis.

## Requirements

- Python 3.x
- `scapy` library (`pip install scapy`)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/network-packet-analyzer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd network-packet-analyzer
    ```

3. Run the packet sniffer:

    ```bash
    python packet_sniffer.py
    ```

4. Watch the captured packets being printed to the console, including source and destination IP addresses, protocol types, and payload data.

## Ethical Use

Ensure that you have proper authorization before using this tool to monitor network traffic. It should only be used on networks that you own or have explicit permission to monitor. Misuse of packet sniffers can violate privacy laws and network policies.
