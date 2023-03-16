from django.db import models

class Work(models.Model):
    name_work = models.CharField(max_length=40, verbose_name='Должность')#verbose_name='Должность' меняет название в api
    class Meta: #Меняет в админке название моделей
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

class Worker(models.Model):
    name = models.CharField(max_length=25, verbose_name='Имя')
    surname = models.CharField(max_length=25, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=25, verbose_name='Отчество')
    login = models.CharField(max_length=50, verbose_name='Логин')
    password = models.CharField(max_length=100, verbose_name='Пароль')
    photo = models.ImageField(verbose_name='Фото')
    work = models.ForeignKey('Work', on_delete=models.PROTECT, null=True, verbose_name='Должность')

    class Meta: #Меняет в админке название моделей
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
class Status(models.Model):
    status = models.CharField(max_length=15, verbose_name='Статус')
    class Meta: #Меняет в админке название моделей
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
class Order(models.Model):
    table = models.CharField(max_length=20, verbose_name='Стол')
    worker = models.ForeignKey('Worker', on_delete=models.PROTECT, null=True, verbose_name='Работник')
    add_order = models.DateTimeField(verbose_name='Время создания заказа')
    status = models.ForeignKey('Status', on_delete=models.PROTECT, null=True, verbose_name='Статус')
    cost = models.IntegerField(max_length=10, verbose_name='Цена')
    class Meta: #Меняет в админке название моделей
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'