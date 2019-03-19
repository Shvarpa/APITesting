import requests
import re

class domain_api:
    @staticmethod
    def get(domain):
        endpoint = "https://api.domainsdb.info/search"
        query = {'query':domain}
        return requests.get(endpoint,query).json()

class Email:
    def __init__(self,email):
        self.email = email 

    def __str__(self):
        return str(self.email)

    def __repr__(self):
        return repr(self.email)

    @staticmethod
    def _match(email):
        return re.match(r"^[a-zA-Z0-9_.+-]+@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$", str(email))

    @property
    def domain(self):
        matches = Email._match(self)
        if not matches: return None
        return matches[1]

    
    def _valid_domain(self):
        domain = self.domain
        if not domain: return False
        res = domain_api.get(domain)
        if res['total'] < 1: return False
        found_dom = res['domains'][0]
        if not re.match(found_dom['domain'],domain) : return False
        if found_dom.get('isDead'):
            if found_dom['isDead'] == True : return False
        return True


    @property
    def is_valid(self):
        in_format = Email._match(self)
        if not in_format: return False
        domain = self.domain
        if not domain: return False
        if not self._valid_domain(): return False
        return True

