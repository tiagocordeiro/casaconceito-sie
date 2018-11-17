from django.contrib.auth.models import AnonymousUser, User, Group
from django.test import RequestFactory, TestCase
from django.utils import timezone

from .views import indicacao_list_dadmin, dashboard
from .models import Indicacao
from .forms import IndicacaoForm


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

    def test_lista_indicacoes_logado(self):
        self.group = Group.objects.create(name='Gerente')
        request = self.factory.get('/indicacoes')
        request.user = self.user

        response = indicacao_list_dadmin(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_parceiro_anonimo(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()

        response = dashboard(request)
        self.assertEqual(response.status_code, 302)

    def test_dashboard_parceiro_logado(self):
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
