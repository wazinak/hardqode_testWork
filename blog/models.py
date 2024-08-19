from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(verbose_name='Описание')
    start_date_time = models.DateTimeField(verbose_name='Дата и время начала')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость', default=0)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('-id',)

    def __str__(self):
        return self.name


class UserAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')

    class Meta:
        unique_together = ('user', 'product')
        verbose_name_plural = 'Доступ к продуктам'

    def __str__(self):
        return f'{self.user.username} есть доступ к {self.product.name}'


class Lesson(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название урока')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    description = models.TextField(verbose_name='Описание урока', null=True, blank=True)
    video_link = models.URLField(verbose_name='Ссылка на видео')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('-id',)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название группы')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    slug = models.SlugField(max_length=200, unique=True)
    students = models.ManyToManyField(User, verbose_name='Список студентов')
    min_users = models.PositiveIntegerField(verbose_name='Минимальное количество студентов')
    max_users = models.PositiveIntegerField(verbose_name='Максимальное количество студентов')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['-name']

    def __str__(self):
        return self.name
