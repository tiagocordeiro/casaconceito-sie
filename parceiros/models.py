from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles/')

    class Meta:
        verbose_name_plural = "Profiles"


class Indicacao(models.Model):
    INDICACAO_STATUS_CHOICES = (
        ('NOVO', 'Novo'),
        ('EM ANDAMENTO', 'Em andamento'),
        ('FECHADO', 'Fechado'),
        ('PERDIDO', 'Perdido'),
    )
    cliente = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey(User,
                                 blank=True, null=True,
                                 on_delete=models.SET_NULL)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=INDICACAO_STATUS_CHOICES, default='NOVO')

    class Meta:
        verbose_name_plural = "indicações"

    def publish(self):
        self.data_criacao = timezone.now()
        self.save()

    def __str__(self):
        return self.cliente
