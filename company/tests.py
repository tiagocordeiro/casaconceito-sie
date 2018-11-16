from django.contrib.auth.models import AnonymousUser, User, Group
from django.test import RequestFactory, TestCase
from django.utils import timezone

from .views import company_details
from .models import Company
from .forms import CompanyForm


class CompanyDertailsViewTestCorretor(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.group = Group.objects.create(name='Corretor')
        self.group.user_set.add(self.user)

    def test_company_details_anonimo(self):
        request = self.factory.get('/company')
        request.user = AnonymousUser()

        response = company_details(request)
        self.assertEqual(response.status_code, 302)

    def test_company_details_logado_como_corretor(self):
        request = self.factory.get('/company')
        request.user = self.user

        response = company_details(request)
        self.assertEqual(response.status_code, 302)


class CompanyDertailsViewTestCompanyAdmin(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.group = Group.objects.create(name='CompanyAdmin')
        self.group.user_set.add(self.user)

    def test_company_details_anonimo(self):
        request = self.factory.get('/company')
        request.user = AnonymousUser()

        response = company_details(request)
        self.assertEqual(response.status_code, 302)

    def test_company_details_logado_como_company_admin(self):
        request = self.factory.get('/company')
        request.user = self.user

        response = company_details(request)
        self.assertEqual(response.status_code, 200)
