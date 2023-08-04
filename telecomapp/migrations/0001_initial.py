# Generated by Django 4.2.3 on 2023-08-01 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelecomAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=250)),
                ('familiya', models.CharField(max_length=250)),
                ('ochistiva', models.CharField(max_length=250)),
                ('mahalla', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TelecomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('router_name', models.CharField(max_length=250)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telecomapp.telecomadmin')),
            ],
        ),
    ]
