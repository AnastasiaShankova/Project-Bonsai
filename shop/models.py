from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Категория")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Plant(models.Model):
    name = models.CharField(max_length=50, verbose_name="Растение")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория")
    description = models.TextField(verbose_name="Описание", blank=True)
    image = models.ImageField(null=True, blank=True,
                              verbose_name="Фото", upload_to="media")
    available_quantity = models.IntegerField()
    price = models.FloatField(blank=True, verbose_name="Стоимость")
    height = models.CharField(blank=True, max_length=50, verbose_name="Высота")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['category', 'name']
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class BasketQuerySet(models.QuerySet):
    def total_qty(self):
        return sum(basket.quantity for basket in self)

    def quantity_in_basket(self):
        return {basket.plant.id: basket.quantity for basket in self}


class Basket(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь")
    plant = models.ForeignKey(
        Plant, on_delete=models.CASCADE, verbose_name="Растение")
    quantity = models.PositiveSmallIntegerField(
        default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания")

    objects = BasketQuerySet.as_manager()

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return f" Корзина для {self.user.username} Продукт: {self.plant.name}"

    def sum(self):
        return self.plant.price * self.quantity


['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
['Nothing', 'will', 'work', 'unless', 'you', 'do']
