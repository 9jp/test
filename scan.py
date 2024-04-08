import socket

def scan_website(url):
    """Scans a website for its IP address and system name."""

    # Get the IP address of the website.
    ip_address = socket.gethostbyname(url)

    # Get the system name of the website.
    system_name = socket.gethostbyaddr(ip_address)[0]

    # Print the IP address and system name of the website.
    print("IP address:", ip_address)
    print("System name:", system_name)

if __name__ == "__main__":
    # Get the URL of the website to scan.
    url = input("Enter the URL of the website to scan: ")

    # Scan the website.
    scan_website(url)
