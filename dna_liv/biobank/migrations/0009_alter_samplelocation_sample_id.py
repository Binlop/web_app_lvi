# Generated by Django 4.1 on 2023-11-05 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biobank', '0008_remove_samplelocation_name_sample_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samplelocation',
            name='sample_id',
            field=models.IntegerField(default=''),
        ),
    ]
