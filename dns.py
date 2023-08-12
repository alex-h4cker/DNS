import socket

def ip_to_url(ip):
    try:
        url = socket.gethostbyaddr(ip)[0]
        return url
    except socket.herror:
        return "Unable to resolve IP to URL"
#chenge
ip = "yur-ip"
url = ip_to_url(ip)
print(f"URL for IP {ip}:
