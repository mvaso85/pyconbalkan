# Generated by Django 2.0.5 on 2018-06-04 13:46

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0002_auto_20180603_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='description',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
