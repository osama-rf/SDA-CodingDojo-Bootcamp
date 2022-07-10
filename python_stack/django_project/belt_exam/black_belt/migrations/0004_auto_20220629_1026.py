# Generated by Django 2.2.4 on 2022-06-29 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('black_belt', '0003_job_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='user',
        ),
        migrations.AddField(
            model_name='job',
            name='user',
            field=models.ManyToManyField(related_name='job', to='black_belt.User'),
        ),
    ]