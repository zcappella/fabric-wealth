from django.forms import ModelForm

from core.models import Widget, Order

class WidgetCreateForm(ModelForm):
	class Meta:
		model = Widget
		fields = [
			'title',
			'size',
			'color',
		]


class OrderCreateForm(ModelForm):
	class Meta:
		model = Order
		fields = [
			'widgets',
		]		
