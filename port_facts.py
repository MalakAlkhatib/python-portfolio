# port_facts.py
# References:
# - RFC 9293: TCP Header Source/Destination Port are 16 bits each.
# - RFC 791: IPv4 addresses are fixed length of 32 bits (four octets).

PORT_BITS = 16
IPV4_BITS = 32

possible_ports = 2 ** PORT_BITS
highest_port = (2 ** PORT_BITS) - 1
possible_ipv4 = 2 ** IPV4_BITS

print(f"Total possible TCP ports: {possible_ports}")
print(f"Highest TCP port number: {highest_port}")
print(f"Total possible IPv4 addresses: {possible_ipv4}")
