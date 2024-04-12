import socket
from ip2geotools.databases.noncommercial import DbIpCity

print("CODED BY MJ, My Website: m-j.sa My Server: Discord.gg/mJm")

url = input("Enter the website link: ")

def get_ip(url):
    ip_address = socket.gethostbyname(url)
    return ip_address

def get_dns(url):
    try:
        dns = socket.gethostbyaddr(socket.gethostbyname(url))[0]
        return dns
    except socket.herror:
        return "Unknown host"

def get_registration_info(url):
    try:
        registration_info = socket.gethostbyaddr(socket.gethostbyname(url))[1]
        domain = registration_info[0] if len(registration_info) >= 1 else "N/A"
        organization = registration_info[1] if len(registration_info) >= 2 else "N/A"
        return domain, organization
    except socket.herror:
        return "N/A", "N/A"

def get_ip_location(ip):
    response = DbIpCity.get(ip, api_key='free')
    city = response.city
    country = response.country
    return city, country

try:
    ip = get_ip(url)
    dns = get_dns(url)
    domain, organization = get_registration_info(url)
    city, country = get_ip_location(ip)

    print("IP Address: ", ip)
    print("DNS Name: ", dns)
    print("Domain: ", domain)
    print("Organization: ", organization)
    print("IP Location - City: {}, Country: {}".format(city, country))

except Exception as e:
    print("An error occurred:", e)
