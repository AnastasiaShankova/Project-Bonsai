# Generated by Django 5.0.2 on 2024-06-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('В обработке', 'В обработке'), ('Оформлен', 'Оформлен'), ('Собран', 'Собран'), ('Доставлен', 'Доставлен'), ('Закрыт', 'Закрыт')], default='В обработке', max_length=50, verbose_name='Статус заказа'),
        ),
    ]
