# Generated by Django 5.1 on 2024-08-19 11:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['-name'], 'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['-name'], 'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-name'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='useraccess',
            options={'verbose_name': 'Доступ к продукту'},
        ),
        migrations.AlterField(
            model_name='group',
            name='max_users',
            field=models.PositiveIntegerField(verbose_name='Максимальное количество студентов'),
        ),
        migrations.AlterField(
            model_name='group',
            name='min_users',
            field=models.PositiveIntegerField(verbose_name='Минимальное количество студентов'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название группы'),
        ),
        migrations.AlterField(
            model_name='group',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='group',
            name='students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Список студентов'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название урока'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video_link',
            field=models.URLField(verbose_name='Ссылка на видео'),
        ),
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='product',
            name='start_date_time',
            field=models.DateTimeField(verbose_name='Дата и время начала'),
        ),
        migrations.AlterField(
            model_name='useraccess',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='useraccess',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterUniqueTogether(
            name='useraccess',
            unique_together={('user', 'product')},
        ),
    ]
