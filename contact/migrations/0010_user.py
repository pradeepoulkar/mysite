# Generated by Django 3.2.13 on 2022-05-17 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_details2'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]
