# Generated by Django 3.2.4 on 2021-10-02 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_auto_20211002_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Home.product')),
                ('brand', models.CharField(max_length=500)),
                ('model_number', models.CharField(max_length=500)),
                ('series', models.CharField(max_length=500)),
                ('model_name', models.CharField(max_length=500)),
                ('slr_variant', models.CharField(max_length=500)),
                ('brand_color', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=500)),
                ('color', models.CharField(max_length=500)),
                ('effective_pixels', models.CharField(max_length=500)),
                ('tripod_socket', models.CharField(max_length=500)),
                ('wifi', models.CharField(max_length=500)),
                ('sensor_type', models.CharField(max_length=500)),
                ('image_sensor_size', models.CharField(max_length=500)),
                ('iso_rating', models.CharField(max_length=500)),
                ('lens_mount', models.CharField(max_length=500)),
                ('dust_reduction', models.CharField(max_length=500)),
                ('focus_points', models.CharField(max_length=500)),
                ('shutter_speed', models.CharField(max_length=500)),
                ('self_timer', models.CharField(max_length=500)),
                ('continuous_shots', models.CharField(max_length=500)),
                ('image_format', models.CharField(max_length=500)),
                ('video_resolution', models.CharField(max_length=500)),
                ('video_quality', models.CharField(max_length=500)),
                ('display_type', models.CharField(max_length=500)),
                ('display_size', models.CharField(max_length=500)),
                ('touch_screen', models.CharField(max_length=500)),
                ('compatible_card', models.CharField(max_length=500)),
                ('battery_type', models.CharField(max_length=500)),
                ('width', models.CharField(max_length=500)),
                ('height', models.CharField(max_length=500)),
                ('depth', models.CharField(max_length=500)),
                ('weight', models.CharField(max_length=500)),
            ],
            bases=('Home.product',),
        ),
        migrations.CreateModel(
            name='Tablets',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Home.product')),
                ('model_number', models.CharField(max_length=500)),
                ('model_name', models.CharField(max_length=500)),
                ('color', models.CharField(max_length=500)),
                ('connectivity', models.CharField(max_length=500)),
                ('os', models.CharField(max_length=500)),
                ('operating_system_version', models.CharField(max_length=500)),
                ('ram', models.CharField(max_length=500)),
                ('voice_call', models.CharField(max_length=500)),
                ('display_resolution_type', models.CharField(max_length=500)),
                ('video_call', models.CharField(max_length=500)),
                ('supported_network', models.CharField(max_length=500)),
                ('battery_features', models.CharField(max_length=500)),
                ('processor_type', models.CharField(max_length=500)),
                ('display_size', models.CharField(max_length=500)),
                ('sales_package', models.CharField(max_length=500)),
                ('display_resolution', models.CharField(max_length=500)),
                ('primary_camera', models.CharField(max_length=500)),
                ('internal_storage', models.CharField(max_length=500)),
                ('processor_speed', models.CharField(max_length=500)),
                ('sim_type', models.CharField(max_length=500)),
                ('battery_capacity', models.CharField(max_length=500)),
                ('battery_type', models.CharField(max_length=500)),
                ('frame_rate', models.CharField(max_length=500)),
                ('bluetooth_version', models.CharField(max_length=500)),
                ('usb', models.CharField(max_length=500)),
                ('wi_fi_version', models.CharField(max_length=500)),
                ('display_type', models.CharField(max_length=500)),
            ],
            bases=('Home.product',),
        ),
    ]