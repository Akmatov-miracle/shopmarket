# Generated by Django 3.2.4 on 2021-06-29 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='dislikes',
            new_name='like',
        ),
        migrations.RemoveField(
            model_name='product',
            name='likes',
        ),
    ]
