# Generated by Django 4.1.8 on 2023-05-18 08:19

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_hijyenmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hijyenmodel',
            name='slug',
            field=autoslug.fields.AutoSlugField(allow_unicode=True, blank=True, editable=False, null=True, populate_from='baslik', unique=True),
        ),
    ]
