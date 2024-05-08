#!/usr/bin/env python
# coding: utf-8

# In[2]:


from scapy.all import *


def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        if protocol == 6:  # TCP protocol
            payload = str(packet[TCP].payload)
            print(f"TCP Packet - Source: {src_ip}, Destination: {dst_ip}, Payload: {payload}")

        elif protocol == 17:  # UDP protocol
            payload = str(packet[UDP].payload)
            print(f"UDP Packet - Source: {src_ip}, Destination: {dst_ip}, Payload: {payload}")

        else:
            print(f"Other Protocol - Source: {src_ip}, Destination: {dst_ip}, Protocol: {protocol}")


def main():
    print("Starting Packet Sniffer...")
    sniff(prn=packet_callback, store=0)


if __name__ == "__main__":
    main()


# In[1]:


get_ipython().system('pip install scapy')


# In[ ]:




