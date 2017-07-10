from django import forms
from django.forms import modelformset_factory

from core.models import Widget, Order, WidgetOrder

############################################
# Form designed to create new widget
############################################
class WidgetCreateForm(forms.ModelForm):
	class Meta:
		model = Widget
		fields = [
			'title',
			'size',
			'color',
		]

############################################
# Form designed to create new order
############################################
class WidgetOrderForm(forms.ModelForm):
	class Meta:
		model = WidgetOrder
		fields = [
			'widget',
			'quantity',
		]


############################################
# Formset designed to handle multiple widgets in an order
############################################
WidgetOrderFormset = modelformset_factory(WidgetOrder, exclude=('order',))