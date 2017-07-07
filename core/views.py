from django.shortcuts import render
from django.views.generic import ListView, CreateView

from core.models import Widget
from core.forms import WidgetCreateForm

# Create your views here.

class WidgetListView(ListView):
	model = Widget
	context_object_name = 'widget'
	template_name = 'core/widget_list.html'

	def get_context_data(self, **kwargs):
		context = super(WidgetListView, self).get_context_data(**kwargs)

		return context


class WidgetCreateView(CreateView):
	model = Widget
	context_object_name = 'widget'
	template_name = 'core/widget_create.html'
	form = WidgetCreateForm