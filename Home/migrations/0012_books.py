# Generated by Django 3.2.4 on 2021-10-03 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0011_fashion_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=500)),
                ('price', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('available_offers', models.TextField(max_length=10000)),
                ('service', models.TextField(max_length=10000)),
                ('seller', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=10000)),
                ('specification', models.TextField(max_length=20000)),
                ('highlights', models.TextField(max_length=10000)),
                ('img1', models.ImageField(upload_to='pic')),
            ],
        ),
    ]
