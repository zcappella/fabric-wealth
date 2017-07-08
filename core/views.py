from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView

from core.models import Widget, Color, Size, Order
from core.forms import WidgetCreateForm, OrderCreateForm

# Create your views here.

class WidgetListView(ListView):
	model = Widget
	context_object_name = 'widget'
	template_name = 'core/widget_list.html'


	def get_context_data(self, **kwargs):
		ctx = super(WidgetListView, self).get_context_data(**kwargs)

		ctx['widgets'] = Widget.objects.all()
		return ctx



class WidgetCreateView(CreateView):
	model = Widget
	context_object_name = 'widget'
	template_name = 'core/widget_create.html'
	form = WidgetCreateForm
	success_url = reverse_lazy('core:widget-list')
	fields = '__all__'

	def get_context_data(self, **kwargs):
		ctx = super(WidgetCreateView, self).get_context_data(**kwargs)

		ctx['colors'] = Color.objects.all()
		ctx['sizes'] = Size.objects.all()

		return ctx


class OrderCreateView(CreateView):
	model = Order
	context_object_name = 'Order'
	template_name = 'core/Order_create.html'
	form = OrderCreateForm
	success_url = reverse_lazy('core:Order-list')
	fields = '__all__'

	def get_context_data(self, **kwargs):
		ctx = super(OrderCreateView, self).get_context_data(**kwargs)

		ctx['colors'] = Color.objects.all()
		ctx['sizes'] = Size.objects.all()
		ctx['widgets'] = Widget.objects.all()

		return ctx		