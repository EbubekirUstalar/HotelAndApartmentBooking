# Generated by Django 3.2 on 2021-12-28 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blocked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_on', models.DateTimeField(blank=True, null=True, verbose_name='date started')),
                ('end_on', models.DateTimeField(blank=True, null=True, verbose_name='date ended')),
                ('booking_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blocked_info', to='listings.bookinginfo')),
            ],
        ),
    ]