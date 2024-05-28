# Generated by Django 5.0.3 on 2024-04-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.EmailField(max_length=254, verbose_name='Email')),
                ('password', models.CharField(default='', max_length=50, verbose_name='Пароль')),
            ],
        ),
    ]
