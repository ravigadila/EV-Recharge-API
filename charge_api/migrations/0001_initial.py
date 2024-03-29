# Generated by Django 4.2.6 on 2023-10-29 15:43

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=200, unique=True, verbose_name='Name Of charging station')),
                ('brand', models.CharField(max_length=200, unique=True, verbose_name='charging station brand')),
                ('phone_number', models.CharField(blank=True, default='', max_length=20, verbose_name='Phone Number of person')),
                ('email', models.EmailField(blank=True, default='', max_length=254, verbose_name='email address of station')),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=55)),
                ('state', models.CharField(blank=True, default='', max_length=55)),
                ('zip_code', models.CharField(blank=True, default='', max_length=20)),
                ('country', models.CharField(max_length=55)),
                ('landmark', models.CharField(blank=True, default='', max_length=100)),
                ('location_point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('notes', models.CharField(blank=True, default='', max_length=1000, verbose_name='Extra details(optional)')),
                ('amenities', models.CharField(blank=True, default='', max_length=255)),
                ('station_type', models.CharField(choices=[('HOME', 'Home'), ('COMMERCIAL', 'Commercial'), ('SHOPPING_MALL', 'SHOPPING_MALL'), ('RESTAURANT', 'RESTAURANT'), ('OTHER', 'OTHER')], default='UNKNOWN', max_length=55)),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('REMOVED', 'REMOVED'), ('MAINTENANCE', 'MAINTENANCE')], default='ACTIVE', max_length=55)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Connector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connector_name', models.CharField(max_length=200, verbose_name='unique code of each point')),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'AVAILABLE'), ('IN_USE', 'IN_USE'), ('COMING_SOON', 'COMING_SOON'), ('IN_REPAIR', 'In Repair/Not Funtioning'), ('REMOVED', 'REMOVED')], default='WORKING', max_length=55)),
                ('cost_per_hr', models.DecimalField(decimal_places=5, default=0, max_digits=5)),
                ('compatibility', models.CharField(blank=True, default='ALL', max_length=255, verbose_name='vehicle name')),
                ('fixed_cable', models.BooleanField(default=False)),
                ('accessibility_type', models.CharField(choices=[('RESTRICTED', 'RESTRICTED'), ('PUBLIC', 'PUBLIC')], default='PUBLIC', max_length=25)),
                ('notes', models.CharField(max_length=255)),
                ('chargeCapacity', models.FloatField(verbose_name='in kW')),
                ('payment_methods', models.CharField(choices=[('FREE', 'FREE'), ('REQUIRE_PAYMENT', 'REQUIRE_PAYMENT'), ('SUBSCRIPTION', 'SUBSCRIPTION')], default='REQUIRE_PAYMENT', max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='charge_api.station')),
            ],
        ),
    ]
