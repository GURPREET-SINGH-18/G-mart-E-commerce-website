# Generated by Django 3.2.4 on 2021-10-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0015_auto_20211006_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fashion',
            name='price',
            field=models.IntegerField(),
        ),
    ]
