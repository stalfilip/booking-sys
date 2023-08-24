# Generated by Django 4.2.4 on 2023-08-19 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0005_remove_resource_availability_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='slots_booked',
            field=models.IntegerField(default=1, verbose_name='Slots Booked'),
        ),
        migrations.AddField(
            model_name='resource',
            name='custom_attributes',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='resource',
            name='duration_hours',
            field=models.FloatField(default=1.0, verbose_name='Duration in Hours'),
        ),
        migrations.CreateModel(
            name='BookingParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_data', models.JSONField(blank=True, default=dict)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.booking', verbose_name='Booking')),
            ],
        ),
        migrations.CreateModel(
            name='ResourcePermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('granted', models.DateTimeField(auto_now_add=True)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.resource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'resource')},
            },
        ),
    ]