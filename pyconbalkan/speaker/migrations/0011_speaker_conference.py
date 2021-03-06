# Generated by Django 2.1.7 on 2019-03-03 16:46

from django.db import migrations, models
import django.db.models.deletion
import pyconbalkan.conference.abstractions


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0007_auto_20190227_0738'),
        ('speaker', '0010_speaker_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='conference',
            field=models.ForeignKey(default=pyconbalkan.conference.models._get_default_conference, on_delete=django.db.models.deletion.CASCADE, to='conference.Conference'),
        ),
    ]
