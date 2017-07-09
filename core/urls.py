from django.conf.urls import url

from core.views import WidgetListView, WidgetCreateView, OrderCreateView, OrderNameCreateView, OrderNameListView, OrderListView

app_name = 'core'
urlpatterns = [
	url(r'^$', WidgetListView.as_view(), name='widget-list'),
	url(r'^widget_create/$', WidgetCreateView.as_view(), name='widget-create'),
	url(r'^order_create/(?P<order_dict>[0-9]+)$', OrderCreateView.as_view(), name='order-create'),
	url(r'^order_title/$', OrderNameCreateView.as_view(), name='order-title'),
	url(r'^order_list/$', OrderListView.as_view(), name='order-list'),
	url(r'^order_title_list/$', OrderNameListView.as_view(), name='order-title-list')
]