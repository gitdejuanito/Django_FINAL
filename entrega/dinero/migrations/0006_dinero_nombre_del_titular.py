# Generated by Django 4.1.5 on 2023-02-01 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinero', '0005_dinero_nombre_banco'),
    ]

    operations = [
        migrations.AddField(
            model_name='dinero',
            name='nombre_del_titular',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
