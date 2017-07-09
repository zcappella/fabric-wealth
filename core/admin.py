from django.contrib import admin

from core.models import Widget, Color, Size, Order, OrderDict

# Register your models here.

admin.site.register(Widget)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Order)
admin.site.register(OrderDict)