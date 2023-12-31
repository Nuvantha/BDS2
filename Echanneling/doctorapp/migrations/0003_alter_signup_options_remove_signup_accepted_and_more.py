# Generated by Django 4.2.6 on 2023-11-04 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapp', '0002_signup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='signup',
            options={},
        ),
        migrations.RemoveField(
            model_name='signup',
            name='accepted',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='accepted_date',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='confirm_password',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='sent_date',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='accepted_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='sent_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
