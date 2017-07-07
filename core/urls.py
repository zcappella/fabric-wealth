from django.conf.urls import url

from core.views import WidgetListView

app_name = 'core'
urlpatterns = [
	url(r'^$', WidgetListView.as_view(), name='home')
]