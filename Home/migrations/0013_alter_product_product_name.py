# Generated by Django 3.2.4 on 2021-10-06 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=500),
        ),
    ]
