# Generated by Django 2.0.5 on 2018-08-03 15:06

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('speaker', '0009_auto_20180801_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
