import psutil
import matplotlib.pyplot as plt

#Define the network interface to monitor
interface = "eth0"
#Retrieve the network usage statistics for the specified interface
net_io_counters=psutil.net_io_counters()
#interface_counters = bet_io_countres.get(interface)
print(net_io_counters)
#Calculate the amount of data recived and sent in MB
bytes_recived=net_io_counters.bytes_recv /1024/1024
byte_sent=net_io_counters.bytes_sent /1024 /1024
#Create a bar chart of the network usage
plt.bar(["Received","Sent"],[bytes_recived,byte_sent])
plt.ylabel("Bandwidth usage (MB)")
plt.title("Network usage for interface {}".format(interface))
plt.show()