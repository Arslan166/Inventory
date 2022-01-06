# Generated by Django 3.2.6 on 2021-10-01 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_items_itemshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150)),
                ('product_type', models.CharField(max_length=25)),
                ('product_description', models.TextField()),
                ('product_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
