# Generated by Django 2.0.7 on 2018-07-07 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parceiros', '0005_indicacao_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicacao',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
