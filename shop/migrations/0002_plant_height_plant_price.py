# Generated by Django 5.0.2 on 2024-05-08 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='height',
            field=models.CharField(blank=True, max_length=50, verbose_name='Высота'),
        ),
        migrations.AddField(
            model_name='plant',
            name='price',
            field=models.FloatField(blank=True, default=1, verbose_name='Стоимость'),
            preserve_default=False,
        ),
    ]
