import requests
import re

class Email:
    def __init__(self,email):
        self.email = email 

    @property
    def domain(self):
        return self.email.split('@')[1]

    @property
    def is_valid(self):
        matches = re.match(	r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",self.email)
        return matches

