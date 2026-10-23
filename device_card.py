# device_card.py
# This program prints a record about a network device.

MAX_CONNECTIONS = 100

device_name = "web-server-01"
device_ip = "192.0.2.20"
service = "HTTPS"
open_port = 443

print("Device:", device_name)
print("IP address:", device_ip)
print("Service:", service)
print("Port:", open_port)
print("Max connections:", MAX_CONNECTIONS)

service = "SSH"
open_port = 22

print("Updated service:", service, "Port:", open_port)




