import requests
import socket

def get_host_name_ip(mail):
    try:
        domain = mail.split('@')[1]
        host_ip = socket.gethostbyname(domain)
        return host_ip
    except:
        return -1

class location_api:

    @staticmethod
    def get(ip):
        endpoint = "https://ipapi.co/{}/json/".format(ip)
        r = requests.get(endpoint).json()
        try:
            r = {'country': r['country'], 'city': r['city']}
        except:
            return "Error"
        return r


def get_mail_location(mail):
    ip = get_host_name_ip(mail)
    if(ip is -1):
        return -1

    # API call
    lst = location_api.get(ip)
    # print("Country of domian: {}".format(lst['country']))
    # print("City of domain: {}".format(lst['city']))
    return lst
