# Generated by Django 4.1 on 2023-11-05 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biobank', '0007_biospecimen_name_storage_sample'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='samplelocation',
            name='name_sample',
        ),
        migrations.AddField(
            model_name='samplelocation',
            name='sample_id',
            field=models.CharField(default='', max_length=250),
        ),
    ]