# Generated by Django 3.1.1 on 2020-09-22 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='data',
            field=models.DateField(verbose_name='Data'),
        ),
    ]