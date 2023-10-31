# Generated by Django 4.1 on 2023-10-31 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biobank', '0004_box_freezer_shelf_samplelocation_box_shelf'),
    ]

    operations = [
        migrations.AddField(
            model_name='samplelocation',
            name='count_col',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='samplelocation',
            name='count_rows',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='samplelocation',
            name='count_samples',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='samplelocation',
            name='name_sample',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='samplelocation',
            name='state_location',
            field=models.CharField(default='free', max_length=10),
        ),
    ]