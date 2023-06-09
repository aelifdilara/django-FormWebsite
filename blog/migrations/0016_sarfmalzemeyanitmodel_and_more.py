# Generated by Django 4.1.8 on 2023-05-20 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0015_alter_hijyenmodel_form_gonderen'),
    ]

    operations = [
        migrations.CreateModel(
            name='SarfMalzemeYanitModel',
            fields=[
                ('malzememodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.malzememodel')),
                ('aciklama', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Sarf Malzeme Yanıt Formu',
                'verbose_name_plural': 'Sarf Malzeme Yanıt Formları',
                'db_table': 'sarf_malzeme_yanit',
            },
            bases=('blog.malzememodel',),
        ),
        migrations.AlterField(
            model_name='hijyenmodel',
            name='form_gonderen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hijyen_formlar', to=settings.AUTH_USER_MODEL),
        ),
    ]
