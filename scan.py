import socket
from ip2geotools.databases.noncommercial import DbIpCity

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
    domain = registration_info[0]
    organization = registration_info[1]
    return domain, organization

def get_ip_location(ip):
    response = DbIpCity.get(ip, api_key='free')
    city = response.city
    country = response.country
    return city, country

ip = get_ip(url)
dns = get_dns(url)
domain, organization = get_registration_info(url)
city, country = get_ip_location(ip)

print("IP Address: ", ip)
print("DNS Name: ", dns)
print("Domain: ", domain)
print("Organization: ", organization)
print("IP Location - City: {}, Country: {}".format(city, country))
