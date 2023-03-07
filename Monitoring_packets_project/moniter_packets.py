import matplotlib.pyplot as plt
from scapy.all import *
# Capture packets for 30 seconds
packets=sniff(timeout=30)
# Extract the protocol type from each packet
protocols = [pkt.sprintf('%IP.proto%')for pkt in packets]
# count the occurrences of each protocol type
counts={}
for proto in protocols:
    if proto not in counts:
        counts[proto]=1
    else:
        counts[proto]+=1

# plot the counts as a bar chart
plt.bar(range(len(counts)), list(counts.values()), align='center')
plt.xticks(range(len(counts)), list(counts.keys()))
plt.xlabel('Protocol')
plt.ylabel('Count')
plt.title('Protocol Distribution')
plt.show()
