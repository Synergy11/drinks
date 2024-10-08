# Generated by Django 5.1 on 2024-09-28 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=160)),
                ('last_name', models.CharField(max_length=150)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_number', models.IntegerField()),
            ],
        ),
    ]
