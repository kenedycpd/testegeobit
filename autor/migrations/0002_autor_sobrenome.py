# Generated by Django 3.1.1 on 2020-09-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='sobrenome',
            field=models.CharField(default=1, max_length=100, verbose_name='Nome'),
            preserve_default=False,
        ),
    ]
