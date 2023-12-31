# Generated by Django 4.2.2 on 2023-06-25 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('periodo', models.CharField(max_length=100, verbose_name='Período')),
                ('nota', models.IntegerField(max_length=3, verbose_name='Nota')),
                ('situacao', models.BooleanField(verbose_name='Situação')),
            ],
        ),
    ]
