# Generated by Django 3.1.7 on 2021-03-05 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20210305_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]
