from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    logo = models.ImageField(upload_to='company/logo/')

    class Meta:
        verbose_name = "dados da empresa"

    def __str__(self):
        return self.name
