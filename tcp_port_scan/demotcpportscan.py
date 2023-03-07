from scapy.all import *
#DEFINE THE target IP address and the range of ports to scan
target_ip="192.168.149.128"
port_range=range(1,100)
#Loop through
for port in port_range:
    packet=IP(dst=target_ip) / TCP(dport=port , flags="S")

    response = sr1(packet, timeout=1, verbose=0)

    if response is not None and response.haslayer(TCP) and response.getlayer(TCP).flag == 0x12:
        print("Port {} is open".format(port))