from django.conf.urls import url

from core.views import WidgetListView, WidgetCreateView

app_name = 'core'
urlpatterns = [
	url(r'^$', WidgetListView.as_view(), name='widget-list'),
	url(r'^widget_create/$', WidgetCreateView.as_view(), name='widget-create')
]