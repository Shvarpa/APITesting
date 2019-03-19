import unittest
import unittest.mock as mock
import src.mail_domain_location as mail_domain_location

class test_Mail_Domain_Location(unittest.TestCase):

    def test_mail_domain_api(self):
        mail_domain_location.location_api.get = mock.MagicMock(return_value = {'country': 'IE', 'city': 'Dublin'})
        res = mail_domain_location.get_mail_location('lior@gmail.com')
        self.assertEqual(res['country'], 'IE')
        self.assertEqual(res['city'], 'Dublin')

    def test_empty_mail(self):
        # not uses the API. exit before
        res = mail_domain_location.get_mail_location('')
        self.assertEqual(res, -1)

    def test_mail_with_two_or_more_AtSign(self):
        # not uses the API. exit before
        res = mail_domain_location.get_mail_location('lior@lior@gmail.com')
        self.assertEqual(res, -1)
        res = mail_domain_location.get_mail_location('lior@lior@gm@ail.com')
        self.assertEqual(res, -1)

    def test_mail_without_Atsign(self):
        # not uses the API. exit before
        res = mail_domain_location.get_mail_location('liorgmail.com')
        self.assertEqual(res, -1)
        # this is not a correct user email
        res = mail_domain_location.get_mail_location('gmail.com')
        self.assertEqual(res, -1)

    def test_Atsign_at_the_end_of_the_mail(self):
        mail_domain_location.location_api.get = mock.Mock(return_value = "Error")
        res = mail_domain_location.get_mail_location('liorgmail.com@')
        self.assertEqual(res, 'Error')
        res = mail_domain_location.get_mail_location('@')
        self.assertEqual(res, 'Error')


