# Generated by Django 3.2.4 on 2021-06-29 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_remove_product_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='like',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
