# Generated by Django 4.1.3 on 2023-02-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkkoutdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(blank=True, max_length=100, null=True)),
                ('Lname', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Scdaddres', models.CharField(blank=True, max_length=100, null=True)),
                ('Landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('Pin', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
