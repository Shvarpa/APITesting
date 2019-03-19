import unittest
from unittest import mock
from src.validate_mail import Email

class test_validate_email(unittest.TestCase):

    def test_bad_email_has_2_at_signs(self):
        email = Email("a@a@a.com")
        print("runaa")
        self.assertFalse(email.is_valid)
    
    