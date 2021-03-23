import socket as s

web_link = input("Enter the url: ")

ip_addr = s.gethostbyname(web_link)

print(ip_addr)


