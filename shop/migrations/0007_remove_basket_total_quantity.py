# Generated by Django 5.0.2 on 2024-05-29 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_basket_total_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='total_quantity',
        ),
    ]
