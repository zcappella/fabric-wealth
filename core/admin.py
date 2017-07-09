from django.contrib import admin

from core.models import Widget, Color, Size, Order, WidgetOrder

# Register your models here.
class WidgetOrderInline(admin.TabularInline):
	model = WidgetOrder


class OrderAdmin(admin.ModelAdmin):
	inlines = [
		WidgetOrderInline,
	]


admin.site.register(Widget)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Order, OrderAdmin)
admin.site.register(WidgetOrder)

