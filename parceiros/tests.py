from django.contrib.auth.models import AnonymousUser, User, Group
from django.test import RequestFactory, TestCase, Client, override_settings
from django.utils import timezone
from django.urls import reverse

from .views import indicacao_list_dadmin, dashboard, signup
from .models import Indicacao
from .forms import IndicacaoForm, SignUpForm


class ParceirosViewsGerenteTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.group = Group.objects.create(name='Gerente')
        self.group.user_set.add(self.user)

    def test_lista_indicacoes_gerente_logado(self):
        request = self.factory.get('/indicacoes')
        request.user = self.user

        response = indicacao_list_dadmin(request)
        self.assertEqual(response.status_code, 200)


class ParceirosViewsCorretorTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.group = Group.objects.create(name='Corretor')
        self.group.user_set.add(self.user)

    def test_lista_indicacoes_anonimo(self):
        request = self.factory.get('/indicacoes')
        request.user = AnonymousUser()

        response = indicacao_list_dadmin(request)
        self.assertEqual(response.status_code, 302)

    def test_dashboard_parceiro_anonimo(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()

        response = dashboard(request)
        self.assertEqual(response.status_code, 302)

    def test_dashboard_parceiro_corretor_logado(self):
        request = self.factory.get('/')
        request.user = self.user

        response = dashboard(request)
        self.assertEqual(response.status_code, 200)


class IndicacoesTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.group = Group.objects.create(name='Corretor')
        self.group.user_set.add(self.user)

    def create_indicacao(self, cliente="Cliente Teste", descricao="Descrição teste"):
        return Indicacao.objects.create(cliente=cliente, descricao=descricao, data_criacao=timezone.now(),
                                        added_by=self.user)

    def test_indicacao_create(self):
        i = self.create_indicacao()
        self.assertTrue(isinstance(i, Indicacao))
        self.assertEqual(i.__str__(), i.cliente)


class IndicacoesFormTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.group = Group.objects.create(name='Corretor')
        self.group.user_set.add(self.user)

    def test_valid_form(self):
        i = Indicacao.objects.create(cliente='Foo', descricao='Bar')
        data = {'cliente': i.cliente, 'descricao': i.descricao, }
        form = IndicacaoForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        i = Indicacao.objects.create(cliente='', descricao='FooBar')
        data = {'cliente': i.cliente, 'descricao': i.descricao, }
        form = IndicacaoForm(data=data)
        self.assertFalse(form.is_valid())

class SignUpTestes(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.group = Group.objects.create(name='Corretor')
        self.group.user_set.add(self.user)

    def test_registration_view_get(self):
        request = self.factory.get(reverse(signup))
        request.user = AnonymousUser()

        response = signup(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Registrar')

    def test_signup_form_is_valid(self):
        form_data = {
            'username': 'newtestuser',
            'first_name': '',
            'last_name': '',
            'email': 'newtestuser@foo.bar',
            'password1': 'ApTeYm1234',
            'password2': 'ApTeYm1234',
        }

        form = SignUpForm(data=form_data)
        self.assertEqual(form.is_valid(), True)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_signup_post(self):
        form_data = {
            'username': 'newtestuser',
            'first_name': 'New',
            'last_name': 'Teste',
            'email': 'newtestuser@foo.bar',
            'password1': 'ApTeYm1234',
            'password2': 'ApTeYm1234',
        }
        self.client.logout()
        response = self.client.post(reverse('signup'), form_data)
        self.assertEqual(User.objects.get(username='newtestuser').first_name, 'New')
        self.assertEqual(response.status_code, 302)


class NovaIndicacaoTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        self.group = Group.objects.create(name='Corretor')
        self.group.user_set.add(self.user)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_nova_indicacao_post(self):
        form_data = {
            'cliente': 'Novo Cliente',
            'email': 'cliente@foo.bar',
            'descricao': 'Apenas um teste',
            'data_criacao': timezone.now,
            'added_by': self.user,
        }

        self.client.force_login(self.user)
        response = self.client.post(reverse('indicacao_add'), form_data)
        indicacao = Indicacao.objects.last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(indicacao.cliente, 'Novo Cliente')
