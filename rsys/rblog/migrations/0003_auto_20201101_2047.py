# Generated by Django 3.1.2 on 2020-11-01 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rblog', '0002_auto_20201101_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='description',
        ),
        migrations.AddField(
            model_name='post',
            name='publish_date',
            field=models.DateField(null=True),
        ),
    ]
