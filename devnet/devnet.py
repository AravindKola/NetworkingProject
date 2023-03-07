from netmiko import ConnectHandler

device={
    "device_type":"cisco_ios",
    "ip":"sandx-iosxe-recomm-1.cisco.com",
    "username":"developer",
    "password":"C1cso12345",
}

connection=ConnectHandler(**device)
print(connection)
out=connection.send_command("show interfaces")
print(out)