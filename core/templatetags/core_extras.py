from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def get_quantity(context, widget):
	widget_map = context['widget_map']
	return widget_map[widget.id] 