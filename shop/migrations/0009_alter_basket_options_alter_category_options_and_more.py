# Generated by Django 5.0.2 on 2024-06-19 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_basket_created_timestamp_alter_basket_plant_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='plant',
            options={'ordering': ['category', 'name'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
