# Generated by Django 4.2.6 on 2023-11-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('confirm_password', models.TextField(blank=True)),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
    ]