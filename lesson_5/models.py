from django.db import models
from datetime import datetime, timedelta

from django.contrib.auth.models import User


class Flower(models.Model):
    count = models.IntegerField(default=0, blank=True, null=True)
    description = models.TextField(null=True)
    delivered_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    could_use_in_bouquet = models.BooleanField(default=True, null=True)
    wiki_page = models.URLField(default="https://www.wiki.ru", name="wiki", unique_for_date="delivered_at", null=True)  # уникальное для даты комбинация даты и поля
    name = models.CharField(max_length=128, unique=True, null=True)  # название цветка уникальное
    def __str__(self):
        return self.name


class Bouquet(models.Model):
    shop = models.Manager()
    fresh_period = models.DurationField(default=timedelta(days=5), null=True, help_text="use this field when"
                                                                             " you need to have information "
                                                                             " about bouquet fresh time")  # будет свежим 5 дней по умолчанию
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField(default=1.0, null=True)
    flowers = models.ManyToManyField(Flower, verbose_name="Этот букет состоит из цветов")


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    second_email = models.EmailField(blank=True)
    name = models.CharField(max_length=64, null=True)
    invoice = models.FileField(null=True, upload_to='uploads/%Y/%m/%d')  # инвойс =  накладная файл
    user_uuid = models.UUIDField(editable=False, null=True)  # нельзя изменить
    discount_size = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    client_ip = models.GenericIPAddressField(blank=True, null=True, protocol="IPv4")

    def __str__(self):
        return self.name





