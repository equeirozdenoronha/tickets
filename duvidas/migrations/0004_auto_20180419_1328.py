# Generated by Django 2.0.4 on 2018-04-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duvidas', '0003_auto_20180419_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='categorias',
            field=models.ManyToManyField(null=True, related_name='categorias', to='duvidas.Categoria'),
        ),
    ]