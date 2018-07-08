from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Indicacao(models.Model):
    cliente = models.CharField(max_length=200)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey(User,
                                 blank=True, null=True,
                                 on_delete=models.SET_NULL)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "indicações"

    def publish(self):
        self.data_criacao = timezone.now()
        self.save()

    def __str__(self):
        return self.cliente
