from django.shortcuts import render
from django.views.generic import ListView, CreateView

from core.models import Widget, Color, Size
from core.forms import WidgetCreateForm

# Create your views here.

class WidgetListView(ListView):
	model = Widget
	context_object_name = 'widget'
	template_name = 'core/widget_list.html'

	def get_context_data(self, **kwargs):
		ctx = super(WidgetListView, self).get_context_data(**kwargs)

		return ctx


class WidgetCreateView(CreateView):
	model = Widget
	context_object_name = 'widget'
	template_name = 'core/widget_create.html'
	form = WidgetCreateForm
	success_url = 'core: "widget-list"'
	fields = '__all__'

	def get_context_data(self, **kwargs):
		ctx = super(WidgetCreateView, self).get_context_data(**kwargs)

		ctx['colors'] = Color.objects.all()
		ctx['sizes'] = Size.objects.all()

		return ctx