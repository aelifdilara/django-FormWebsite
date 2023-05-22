# Generated by Django 4.1.8 on 2023-05-22 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_hijyenyanitmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TasimaYanitModel',
            fields=[
                ('gorevlimodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.gorevlimodel')),
                ('aciklama', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Taşıma Yanıt Formu',
                'verbose_name_plural': 'Taşıma Yanıt Formları',
                'db_table': 'tasima_yanit',
            },
            bases=('blog.gorevlimodel',),
        ),
        migrations.RemoveField(
            model_name='hijyenmodel',
            name='gorevli_kisi',
        ),
        migrations.RemoveField(
            model_name='tasimamodel',
            name='gorevli_kisi',
        ),
    ]
