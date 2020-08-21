from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

from roomate_app.models import Apartment, MyUser
from roomate_app.views import new_apt, assign_apt

class AptTests(TestCase):
    def setUp(self):
        self.auth_user1 = User.objects.create(username='user1')
        self.auth_user1.set_password('abc123456789')
        self.auth_user2 = User.objects.create(username='user2')
        self.auth_user2.set_password('abc123456789')
        self.auth_user1.save()
        self.auth_user2.save()

        self.dummy_apartment = Apartment.objects.create()


    def test_new_apartment(self):
        self.client.login(username='user1', password='abc123456789')
        _ = self.client.post('/newapt/', {})
        self.auth_user1 = User.objects.get(pk=1)
        self.assertIsNotNone(self.auth_user1.myuser.myApt)
    
    def test_join_apartment(self):
        self.client.login(username='user2', password='abc123456789')
        _ = self.client.post('/joinapt/', {'apt_token':self.dummy_apartment.token})
        self.auth_user2 = User.objects.get(pk=2)
        self.assertIsNotNone(self.auth_user2.myuser.myApt)

    def test_new_apartment_sad(self):
        self.client.login(username='user1', password='abc123456789')
        response = self.client.get('/newapt/', {})
        warning = list(get_messages(response.wsgi_request))
        self.assertEqual('Failed To Create An Apartment. Please try again.', str(warning[0]))
    
    def test_join_apartment_sad(self):
        self.client.login(username='user1', password='abc123456789')
        response = self.client.get('/joinapt/', {})
        warning = list(get_messages(response.wsgi_request))
        self.assertEqual('Failed To Join An Apartment. Please Verify Your Token.', str(warning[0]))