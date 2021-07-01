# Generated by Django 3.1.3 on 2021-06-21 13:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_tentative_start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='request_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]