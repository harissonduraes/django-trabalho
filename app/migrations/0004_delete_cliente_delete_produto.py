# Generated by Django 4.2.2 on 2023-06-25 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_aluno'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]
