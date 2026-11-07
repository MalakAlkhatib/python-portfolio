# port_report.py
# Generate a port report for a given range of ports.

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

ports_checked = 0
for port in range(start_port, end_port + 1):
    if port < 1024:
        port_type = "system"
    elif port <= 49151:
        port_type = "user"
    else:
        port_type = "dynamic"
    print(f"{port}: {port_type}")
    ports_checked += 1

print(f"Ports checked: {ports_checked}")
