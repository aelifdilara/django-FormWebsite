# Generated by Django 4.1.8 on 2023-05-18 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_sarfmalzememodel_kategori_adi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hijyenmodel',
            name='idari_calisan',
            field=models.CharField(choices=[('Pınar Hanım', 'Pınar Hanım'), ('Bahar Hanım', 'Bahar Hanım')], default='Pınar Hanım', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sarfmalzememodel',
            name='idari_calisan',
            field=models.CharField(choices=[('Pınar Hanım', 'Pınar Hanım'), ('Bahar Hanım', 'Bahar Hanım')], default='Bahar Hanım', max_length=50, null=True),
        ),
    ]
