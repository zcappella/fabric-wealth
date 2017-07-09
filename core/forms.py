from django import forms

from core.models import Widget, Order, OrderDict

class WidgetCreateForm(forms.ModelForm):
	class Meta:
		model = Widget
		fields = [
			'title',
			'size',
			'color',
		]


class OrderCreateForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = [
			'widgets',
		]
		widgets = {'containter': forms.HiddenInput()}


class OrderDictCreateForm(forms.ModelForm):
	class Meta:
		model = OrderDict
		fields = [
			'order_name',
		]
