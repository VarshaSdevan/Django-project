# Generated by Django 3.1.7 on 2021-03-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_venue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Full Name')),
                ('address', models.CharField(max_length=300)),
                ('email_address', models.EmailField(blank=True, max_length=254, verbose_name='Email Address')),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
