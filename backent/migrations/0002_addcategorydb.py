# Generated by Django 4.1.3 on 2023-01-19 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addcategorydb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.CharField(blank=True, max_length=500, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='profile')),
            ],
        ),
    ]
