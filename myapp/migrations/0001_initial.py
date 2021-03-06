# Generated by Django 3.2.6 on 2021-09-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TimeField()),
                ('date', models.DateField()),
            ],
        ),
    ]
