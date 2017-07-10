from django.conf.urls import url

from core.views import WidgetListView, WidgetCreateView, WidgetOrderCreateView, WidgetOrderEditView, WidgetOrderDeleteView, OrderListView

app_name = 'core'

############################################
# Urls to route the views to 
############################################
urlpatterns = [
	url(r'^$', WidgetListView.as_view(), name='widget-list'),
	url(r'^widget_create/$', WidgetCreateView.as_view(), name='widget-create'),
	url(r'^order_create/$', WidgetOrderCreateView, name='order-create'),
	url(r'^order_edit/(?P<id>\d+)/', WidgetOrderEditView, name='order-edit'),
	url(r'^order_delete/(?P<id>\d+)/', WidgetOrderDeleteView, name='order-delete'),
	url(r'^order_list/$', OrderListView.as_view(), name='order-list'),

]