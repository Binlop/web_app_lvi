# Generated by Django 4.1 on 2023-10-29 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biobank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biospecimen',
            name='file',
            field=models.FileField(default='', upload_to='upldfile/'),
            preserve_default=False,
        ),
    ]
