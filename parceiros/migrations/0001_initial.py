# Generated by Django 2.0.4 on 2018-04-17 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parceiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=200)),
                ('nome', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=300)),
                ('telefone', models.CharField(max_length=30)),
                ('proposta', models.CharField(max_length=350)),
                ('tipo', models.CharField(max_length=40)),
            ],
        ),
    ]
