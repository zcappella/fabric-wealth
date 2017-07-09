from django import forms
from django.forms import modelformset_factory

from core.models import Widget, Order, WidgetOrder

class WidgetCreateForm(forms.ModelForm):
	class Meta:
		model = Widget
		fields = [
			'title',
			'size',
			'color',
		]

class WidgetOrderForm(forms.ModelForm):
	class Meta:
		model = WidgetOrder
		fields = [
			'widget',
			'quantity',
		]


WidgetOrderFormset = modelformset_factory(WidgetOrder, exclude=('order',))