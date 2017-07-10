from django import template

register = template.Library()

@register.simple_tag(takes_context=True)

############################################
# This is a function to allow the template to access the quantity of a widget in an order
############################################
def get_quantity(context, widget):
	widget_map = context['widget_map']
	return widget_map[widget.id] 