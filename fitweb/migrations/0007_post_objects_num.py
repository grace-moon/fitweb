# Generated by Django 3.2.5 on 2021-11-26 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitweb', '0006_delete_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='objects_num',
            field=models.CharField(default='', max_length=200),
        ),
    ]
