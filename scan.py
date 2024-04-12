import socket

url = input("Enter the website link: ")

def get_ip(url):
    ip_address = socket.gethostbyname(url)
    return ip_address

def get_dns(url):
    dns = socket.gethostbyname_ex(url)[-1]
    return dns

ip = get_ip(url)
dns = get_dns(url)

print("IP Address: ", ip)
print("DNS: ", dns)
