# fix the rules

role = "admin"
port = 80
admin = (role == "admin")
port_ok = (port == 80) or (port == 443)

system_port = (port == 22) or (port == 80)
web_port = (port == 80) or (port == 443)

print("Role:", role)
print("Port:", port)
print("Admin:", admin)
print("System port:", system_port)
print("Web port:", web_port)
