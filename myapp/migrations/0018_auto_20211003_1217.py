# Generated by Django 3.2.6 on 2021-10-03 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_remove_shop_tags'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
