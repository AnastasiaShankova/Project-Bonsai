from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to='users_images',
                              null=True, blank=True, verbose_name="Аватар")
    phone_number = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
['Nothing', 'will', 'work', 'unless', 'you', 'do']
