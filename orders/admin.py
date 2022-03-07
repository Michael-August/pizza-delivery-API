from django.contrib import admin
from .models import Order

# Register your models here.
# Note, U must register the model as below for the customization to work
@admin.register(Order)

# Customizing the admin side for Orders
class OrderAdmin(admin.ModelAdmin):
    list_display = ['size', 'order_status', 'quantity', 'created_at']
    list_filter = ['created_at', 'order_status', 'size']