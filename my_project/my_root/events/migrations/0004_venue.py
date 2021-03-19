# Generated by Django 3.1.7 on 2021-03-16 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210310_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=300)),
                ('zip_code', models.CharField(max_length=12, verbose_name='Zip/Post Code')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Contact Phone')),
                ('web', models.URLField(blank=True, verbose_name='Web Address')),
                ('email_address', models.EmailField(blank=True, max_length=254, verbose_name='Email Address')),
            ],
        ),
    ]
