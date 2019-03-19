import unittest
from unittest import mock
from src.validate_mail import Email

class test_validate_email(unittest.TestCase):

    def test_bad_email_has_2_at_signs(self):
        bad_email_two_at_signs = Email("a@a")
        bad_email_no_at_sign = Email("aa")
        self.assertFalse(bad_email_two_at_signs.is_valid)
        self.assertFalse(bad_email_no_at_sign.is_valid)
    
    def test_email_should_have_dot_in_domain(self):
        bad_email=Email('a@gmail')
        self.assertFalse(bad_email.is_valid)

    def test_good_email_should_have_valid_domain_format(self):
        email = Email("a@sce.ac.il")
        self.assertTrue(email.is_valid)

    @mock.patch("src.validate_mail.domain_api",**{"get.return_value": {"total":0,"domains":[]}})
    def test_email_with_unfound_domain_is_bad(self,*args):
        email = Email("a@sce.ac.il")
        self.assertFalse(email.is_valid)

    @mock.patch("src.validate_mail.domain_api",**{"get.return_value": {"total":1,"domains":[{"domain":"sce.ac.il"}]}})
    def test_email_with_found_domain_not_matching_domain(self,*args):
        email = Email("a@sce.bc.il")
        self.assertFalse(email.is_valid)



if __name__ == "__main__":
    unittest.main()