# Generated by Django 2.0.5 on 2018-06-01 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20180601_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, help_text='Enter a description of an item', max_length=500, null=True),
        ),
    ]