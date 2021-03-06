# Generated by Django 2.0.4 on 2018-04-18 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCategoria', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=250)),
                ('resposta', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='categoria',
            name='perguntas',
            field=models.ManyToManyField(to='duvidas.Pergunta'),
        ),
    ]
