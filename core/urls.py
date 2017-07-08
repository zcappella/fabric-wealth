from django.conf.urls import url

from core.views import WidgetListView, WidgetCreateView, OrderCreateView

app_name = 'core'
urlpatterns = [
	url(r'^$', WidgetListView.as_view(), name='widget-list'),
	url(r'^widget_create/$', WidgetCreateView.as_view(), name='widget-create'),
	url(r'^order_create/$', OrderCreateView.as_view(), name='order-create')
]