# Generated by Django 4.0.4 on 2024-02-26 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='password',
            new_name='name',
        ),
    ]
