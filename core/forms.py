from django.forms import ModelForm

from core.models import Widget

class WidgetCreateForm(ModelForm):
	class Meta:
		model = Widget
		fields = [
			'title',
			'size',
			'color',
			'inventory_number',
		]
