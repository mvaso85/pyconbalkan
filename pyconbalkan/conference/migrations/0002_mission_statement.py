# Generated by Django 2.0.5 on 2018-06-21 15:07

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MissionStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('content', markdownx.models.MarkdownxField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]