# Generated by Django 3.2.4 on 2021-10-26 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0016_alter_fashion_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='fashion',
            name='company_name',
            field=models.CharField(default='NA', max_length=100),
            preserve_default=False,
        ),
    ]
