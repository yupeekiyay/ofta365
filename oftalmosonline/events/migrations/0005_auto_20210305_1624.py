# Generated by Django 3.1.7 on 2021-03-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20210305_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
