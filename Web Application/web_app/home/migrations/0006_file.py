# Generated by Django 5.0.1 on 2024-02-06 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_users_table_usersregistry'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
