import socket
import art

from art import
   tprint("MJ")

print("CODED BY MJ, My Website: m-j.sa My Server: Discord.gg/mJm")

url = input("Enter the website link: ")

def get_ip(url):
    ip_address = socket.gethostbyname(url)
    return ip_address

def get_dns(url):
    dns = socket.gethostbyaddr(socket.gethostbyname(url))[0]
    return dns

def get_registration_info(url):
    registration_info = socket.gethostbyaddr(socket.gethostbyname(url))[1]
    return registration_info

ip = get_ip(url)
dns = get_dns(url)
registration_info = get_registration_info(url)

print("IP Address: ", ip)
print("DNS Name: ", dns)
print("Registration Info: ", registration_info)
