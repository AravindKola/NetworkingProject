from scapy.all import *

# Filter packets based on IP address and protocol
packets = sniff(filter="ip and tcp", count=100)

# Save captured packets to a file
wrpcap('captured_packets.pcap', packets)