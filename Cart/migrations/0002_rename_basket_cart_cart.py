# Generated by Django 3.2.4 on 2021-06-29 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='basket',
            new_name='cart',
        ),
    ]
