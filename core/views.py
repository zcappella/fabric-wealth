import requests

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, CreateView

from core.models import Widget, Color, Size, Order, WidgetOrder
from core.forms import WidgetCreateForm, WidgetOrderForm

# Create your views here


############################################
# Class Based Generic List View designed to list the Widgets that have been created
############################################
class WidgetListView(ListView):
	model = Widget
	context_object_name = 'widget'
	template_name = 'core/widget_list.html'


	def get_context_data(self, **kwargs):
		ctx = super(WidgetListView, self).get_context_data(**kwargs)

		ctx['widgets'] = Widget.objects.all()
		return ctx


############################################
# Class Based Generic Create View designed to create new Widgets
############################################
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


############################################
# Class Based Generic List View designed to list the Orders that have been created
############################################
class OrderListView(ListView):
	model = Order
	context_object_name = 'order'
	template_name = 'core/order_list.html'

	# Pass the orders to the context for rendering
	def get_context_data(self, **kwargs):
		ctx = super(OrderListView, self).get_context_data(**kwargs)

		ctx['orders'] = Order.objects.all()

		return ctx


############################################
# Function Based Create View to handle the creation of new Widget Orders
############################################
def WidgetOrderCreateView(request):
	# If you are accessing the page, pass the widgets that are available for order to the context
	if request.method == "GET":
		ctx = {}
		ctx['widgets'] = Widget.objects.all()
		return render(request, 'core/order_create.html', ctx)

	# If you are posting the form, save the widgets in the widget order
	if request.method == "POST":
		order = Order.objects.create()

		for key, val in request.POST.items():
			if val and key != 'csrfmiddlewaretoken':
				widget = Widget.objects.get(id=int(key))
				WidgetOrder.objects.create(widget=widget, order=order, quantity=int(val))

		return redirect('core:order-list')


############################################
# Function Based Edit View to handle the editing of a specific Widget Order
############################################
def WidgetOrderEditView(request, id):
	# If you are accessing the page, pass the widgets that are available for order to the context with a map to access quantity
	if request.method == "GET":
		order = Order.objects.get(id=id)
		ctx = {}
		ctx['order'] = order
		ctx['widgets'] = Widget.objects.all()
		ctx['widget_map'] = {widget.id:widget.quantity for widget in WidgetOrder.objects.filter(order=id)}

		return render(request, 'core/order_edit.html', ctx)

	# If you are posting the form, update the widgets in the widget order
	if request.method == "POST":
		order = Order.objects.get(id=id)

		for key, val in request.POST.items():
			if val and key != 'csrfmiddlewaretoken':
				widget_list =  order.widgets.values_list('id', flat=True)

				if key in widget_list:
					wo = WidgetOrder.objects.get(order=id, widget=int(key))
					wo.quantity = int(val)
					wo.save()

		return redirect('core:order-list')

	# If you are deleting the order, delete the widget order
	if request.method == "DELETE":
		order = Order.objects.get(id=id)
		order.delete()

		return redirect('core:order-list')


############################################
# Function Based Delete View to handle the deletion of a specific Widget Order
############################################
def WidgetOrderDeleteView(request, id):
	if request.method == "POST":
		order = Order.objects.get(id=id)
		order.delete()

		return redirect('core:order-list')

