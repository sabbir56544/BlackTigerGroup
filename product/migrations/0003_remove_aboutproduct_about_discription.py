# Generated by Django 3.1.5 on 2021-01-07 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_aboutproduct_about_discription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutproduct',
            name='about_discription',
        ),
    ]
