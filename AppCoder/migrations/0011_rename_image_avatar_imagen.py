# Generated by Django 4.1.7 on 2023-05-02 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0010_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='image',
            new_name='imagen',
        ),
    ]