# Generated by Django 4.1 on 2023-11-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biobank', '0006_biospecimen_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='biospecimen',
            name='name_storage_sample',
            field=models.CharField(default='', max_length=100, verbose_name='Место хранения образца в хранилище'),
        ),
    ]
