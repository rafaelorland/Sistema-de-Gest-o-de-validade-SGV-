# Generated by Django 5.1 on 2024-08-25 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do Cliente')),
                ('cpf_cnpj', models.CharField(max_length=20, unique=True, verbose_name='CPF/CNPJ')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email do Cliente')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='TelefoneCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=14, verbose_name='Número de Telefone')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Telefone do Cliente',
                'verbose_name_plural': 'Telefones dos Clientes',
            },
        ),
    ]
