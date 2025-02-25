
from django.contrib import admin
from testapp.models import Order  # Импорт модели Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'total_price']  # Поля для отображения
    filter_horizontal = ['items']  # Для удобного выбора товаров

admin.site.register(Order, OrderAdmin)  # Регистрация модели

# admin.py
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active', 'created_at', 'total_price']
    list_filter = ['is_active']