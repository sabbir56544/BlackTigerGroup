# Generated by Django 3.1.5 on 2021-01-09 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_aboutproduct_about_discription'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
