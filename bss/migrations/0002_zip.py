# Generated by Django 4.1.1 on 2023-01-26 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bss', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngoname', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=6)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('contactNumber', models.CharField(max_length=10, unique=True)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
