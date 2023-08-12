# Generated by Django 4.2.4 on 2023-08-12 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resurs',
            name='pris',
            field=models.IntegerField(default=0, verbose_name='Pris'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resurs',
            name='valuta',
            field=models.CharField(default='SEK', max_length=50, verbose_name='Valuta'),
        ),
        migrations.AddField(
            model_name='resurs',
            name='varaktighet',
            field=models.IntegerField(default=0, verbose_name='Varaktighet'),
            preserve_default=False,
        ),
    ]