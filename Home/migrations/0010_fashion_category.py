# Generated by Django 3.2.4 on 2021-10-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_fashion'),
    ]

    operations = [
        migrations.AddField(
            model_name='fashion',
            name='category',
            field=models.CharField(default='Not Provided', max_length=500),
            preserve_default=False,
        ),
    ]