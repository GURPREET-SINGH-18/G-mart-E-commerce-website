# Generated by Django 3.2.4 on 2021-10-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_camera_tablets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fashion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('price', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('available_offers', models.TextField(max_length=10000)),
                ('service', models.TextField(max_length=10000)),
                ('color', models.CharField(max_length=500)),
                ('size', models.CharField(max_length=500)),
                ('seller', models.CharField(max_length=500)),
                ('product_details', models.TextField(max_length=20000)),
                ('img1', models.ImageField(upload_to='pic')),
                ('img2', models.ImageField(upload_to='pic')),
                ('img3', models.ImageField(upload_to='pic')),
                ('img4', models.ImageField(upload_to='pic')),
                ('img5', models.ImageField(upload_to='pic')),
            ],
        ),
    ]
