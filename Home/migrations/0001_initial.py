# Generated by Django 3.2.4 on 2021-10-02 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('price', models.IntegerField()),
                ('offers', models.TextField(max_length=10000)),
                ('warranty', models.TextField(max_length=10000)),
                ('highlights', models.TextField(max_length=100000)),
                ('easy_payment_opt', models.CharField(max_length=100000)),
                ('seller', models.CharField(max_length=10000)),
                ('description', models.TextField(max_length=100000)),
                ('in_the_box', models.CharField(max_length=10000)),
                ('model_no', models.CharField(max_length=1000)),
                ('product_description', models.TextField(max_length=100000)),
                ('company_name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Television',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Home.product')),
                ('display_size', models.CharField(max_length=20)),
                ('screen_type', models.CharField(max_length=10)),
                ('hd_technology_resolution', models.CharField(max_length=20)),
                ('series', models.CharField(max_length=20)),
                ('smart_tv', models.CharField(max_length=20)),
                ('hdmi', models.CharField(max_length=20)),
                ('usb', models.CharField(max_length=20)),
                ('launch_year', models.CharField(max_length=10)),
                ('wall_mount_included', models.CharField(max_length=10)),
                ('picture_engine', models.CharField(max_length=20)),
                ('picture_and_picture', models.CharField(max_length=10)),
                ('view_angle', models.CharField(max_length=10)),
                ('led_display_type', models.CharField(max_length=20)),
                ('aspect_ratio', models.CharField(max_length=10)),
                ('refresh_rate', models.CharField(max_length=10)),
                ('supported_video_formats', models.CharField(max_length=10)),
                ('number_of_speakers', models.CharField(max_length=10)),
                ('speaker_type', models.CharField(max_length=10)),
                ('sound_technology', models.CharField(max_length=20)),
                ('speaker_output', models.CharField(max_length=10)),
                ('sound_mode', models.CharField(max_length=100)),
                ('processor', models.CharField(max_length=10)),
                ('graphic_processor', models.CharField(max_length=50)),
                ('ram_capacity', models.CharField(max_length=10)),
                ('storage_memory', models.CharField(max_length=10)),
                ('supported_app_netflix', models.CharField(max_length=10)),
                ('supported_app_youtube', models.CharField(max_length=10)),
                ('supported_app_disneyplushotstar', models.CharField(max_length=10)),
                ('supported_app_prime_video', models.CharField(max_length=10)),
                ('supported_app_others', models.CharField(max_length=10)),
                ('supported_mobile_operating_system', models.CharField(max_length=10)),
                ('operating_system_present', models.CharField(max_length=10)),
                ('operating_system', models.CharField(max_length=10)),
                ('screen_mirroring', models.CharField(max_length=10)),
                ('app_store_type', models.CharField(max_length=10)),
                ('content_providers', models.CharField(max_length=1000)),
                ('supported_devices_for_casting', models.CharField(max_length=10)),
                ('system_languages', models.CharField(max_length=10)),
                ('bluetooth', models.CharField(max_length=10)),
                ('built_in_wifi', models.CharField(max_length=10)),
                ('ethernet', models.CharField(max_length=10)),
                ('headphone_jack', models.CharField(max_length=10)),
                ('color_screen', models.CharField(max_length=10)),
                ('rf_capable', models.CharField(max_length=10)),
                ('led_backlit_buttons', models.CharField(max_length=10)),
                ('power_requirement', models.CharField(max_length=30)),
                ('power_consumption', models.CharField(max_length=10)),
                ('clock', models.CharField(max_length=10)),
                ('auto_power_off', models.CharField(max_length=10)),
                ('sleep_timer', models.CharField(max_length=10)),
                ('on_off_timer', models.CharField(max_length=10)),
                ('child_lock', models.CharField(max_length=10)),
                ('parental_control', models.CharField(max_length=10)),
                ('width_height_depth', models.CharField(max_length=40)),
                ('weight', models.CharField(max_length=20)),
                ('stand_type', models.CharField(max_length=15)),
                ('additional_features', models.CharField(max_length=20)),
                ('warranty_summary', models.CharField(max_length=50)),
                ('covered_in_warranty', models.CharField(max_length=30)),
                ('not_covered_in_warranty', models.TextField(max_length=10000)),
                ('warranty_service_type', models.CharField(max_length=30)),
                ('installation_demo_details', models.TextField(max_length=10000)),
                ('img1', models.ImageField(upload_to='pic')),
                ('img2', models.ImageField(upload_to='pic')),
                ('img3', models.ImageField(upload_to='pic')),
                ('img4', models.ImageField(upload_to='pic')),
                ('img5', models.ImageField(upload_to='pic')),
            ],
            bases=('Home.product',),
        ),
    ]
