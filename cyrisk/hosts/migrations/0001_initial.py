# Generated by Django 3.2.16 on 2022-10-27 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('criticality', models.CharField(max_length=50)),
            ],
        ),
    ]
