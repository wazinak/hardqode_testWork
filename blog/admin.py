from django.contrib import admin
from .models import UserAccess, Product, Group, Lesson


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'author', 'description', 'start_date_time', 'price']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(UserAccess)
class UserAccessAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'min_users', 'max_users']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'product', 'video_link']
