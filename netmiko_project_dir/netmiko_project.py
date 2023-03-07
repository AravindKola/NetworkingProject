from netmiko import ConnectHandler
#define the device informatrion
device={
    'device_type':'linux',
    'ip':'192.168.149.129',
    'username':'aravind',
    'password':'aravind05',

}
#create a Netmiko SSH connection to the device
connection=ConnectHandler(**device)
#send the "show process cpu" command and capture the output
cpu_output=connection.send_command('cat /proc/cpuinfo')
#send the "show memory statistics" command and capture the output
mem_output=connection.send_command('free -h')
#close the Netmiko SSH connection
connection.disconnect()

#print the CPU and memory output
print('CPU Information:')
print(cpu_output)
print('\nMemory Information:')
print(mem_output)