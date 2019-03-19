import requests
import socket

def get_host_name_ip(mail):
    try:
        domain = mail.split('@')[1]
        host_ip = socket.gethostbyname(domain)
        return host_ip
    except:
        print("Unable to get Hostname and IP")

def get_mail_location(mail):
    ip = get_host_name_ip(mail)
    endpoint = "https://ipapi.co/{}/json/".format(ip)
    r = requests.get(endpoint).json()
    lst = [r['country'], r['city']]
    print("Country of domian: {}".format(lst[0]))
    print("City of domain: {}".format(lst[1]))
    return lst

get_mail_location('weww@walla.co.il')