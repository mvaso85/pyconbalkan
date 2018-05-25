# Generated by Django 2.0.5 on 2018-05-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('level', models.CharField(choices=[('Keystone', 'keystone'), ('Platinum', 'platinum'), ('Gold', 'gold'), ('Silver', 'silver'), ('Partner', 'partner')], max_length=16)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='static/img/sponsors')),
            ],
        ),
    ]