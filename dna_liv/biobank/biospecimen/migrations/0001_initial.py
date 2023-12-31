# Generated by Django 4.1 on 2023-11-09 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biospecimen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='Название образца')),
                ('test_field', models.CharField(default='', max_length=250, verbose_name='Тестовое поле')),
                ('date', models.DateTimeField(verbose_name='Дата получения')),
                ('file_name', models.CharField(max_length=55, verbose_name='Название файла')),
                ('file', models.FileField(upload_to='upldfile/')),
                ('name_storage_sample', models.CharField(default='', max_length=100, verbose_name='Место хранения образца в хранилище')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.samplelocation')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
            options={
                'verbose_name': 'Биологический образец',
                'verbose_name_plural': 'Биологические образцы',
            },
        ),
    ]
