import requests

from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, CreateView

from core.models import Widget, Color, Size, Order, OrderDict
from core.forms import WidgetCreateForm, OrderCreateForm, OrderDictCreateForm

# Create your views here.


def _calculate_widget_ranges():
	widgets = Widget.objects.all()
	range_dict = {}

	for widget in widgets:
		range_dict[widget.id] = 'x' * widget.inventory_number

	return range_dict



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


class OrderNameCreateView(CreateView):
	model = OrderDict
	context_object_name = 'order_dict'
	template_name = 'core/order_title.html'
	form = OrderDictCreateForm
	fields = '__all__'
	success_url = reverse_lazy('core:order-title-list')


class OrderListView(ListView):
	model = OrderDict
	context_object_name = 'order_dict'
	template_name = 'core/order_list.html'

	def get_context_data(self, **kwargs):
		ctx = super(OrderListView, self).get_context_data(**kwargs)

		ctx['order_titles'] = OrderDict.objects.values_list('order_name', flat=True)

		return ctx


class OrderNameListView(ListView):
	model = OrderDict
	context_object_name = 'order_dict'
	template_name = 'core/order_title_list.html'

	def get_context_data(self, **kwargs):
		ctx = super(OrderNameListView, self).get_context_data(**kwargs)

		ctx['order_titles'] = OrderDict.objects.all()

		return ctx



class OrderCreateView(CreateView):
	model = Order
	context_object_name = 'order'
	template_name = 'core/order_create.html'
	form = OrderCreateForm
	success_url = reverse_lazy('core:order-list')
	fields = '__all__'


	def get_context_data(self, **kwargs):
		ctx = super(OrderCreateView, self).get_context_data(**kwargs)

		order_id = self.kwargs['order_dict']

		ctx['colors'] = Color.objects.all()
		ctx['sizes'] = Size.objects.all()
		ctx['widgets'] = Widget.objects.all()
		ctx['ranges'] = _calculate_widget_ranges()
		ctx['container'] = order_id
		ctx['current_orders'] = Order.objects.filter(container=order_id).prefetch_related('widgets')

		return ctx


