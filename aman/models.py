from django.db import models

# Create your models here.

class Settings(models.Model):
    title = models.CharField(max_length= 100 ,verbose_name="Название сайта")
    description = models.TextField(verbose_name="Описание")
    logo = models.ImageField(verbose_name="Логотип сайта")
    icon = models.ImageField(verbose_name="Иконка сайта")
    email = models.EmailField(verbose_name="Контактный email")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    locate = models.CharField(max_length=100 , verbose_name="Адрес")

    

    class Meta:
        verbose_name = "Настройка сайта"
        verbose_name_plural = "Настройки сайта"