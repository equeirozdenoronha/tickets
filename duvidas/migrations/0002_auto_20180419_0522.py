# Generated by Django 2.0.4 on 2018-04-19 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('duvidas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='perguntas',
        ),
        migrations.AddField(
            model_name='pergunta',
            name='categorias',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='duvidas.Categoria'),
        ),
    ]
