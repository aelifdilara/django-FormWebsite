# Generated by Django 4.1.8 on 2023-05-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_hijyenmodel_kategori_adi'),
    ]

    operations = [
        migrations.AddField(
            model_name='sarfmalzememodel',
            name='kategori_adi',
            field=models.CharField(default='Sarf Malzeme', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tasimamodel',
            name='kategori_adi',
            field=models.CharField(default='Taşıma', max_length=50, null=True),
        ),
    ]