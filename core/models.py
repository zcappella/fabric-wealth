from django.db import models

# Create your models here.

############################################
# This will hold all of the possible sizes of a Widget
############################################
class Size(models.Model):
	size = models.CharField(max_length=25)

	def __str__(self):
		return self.size


############################################
# This will hold all of the possible colors of a Widget
############################################
class Color(models.Model):
	color = models.CharField(max_length=25)

	def __str__(self):
		return self.color


############################################
# This will hold the Widget data, along with the title
############################################
class Widget(models.Model):
	title = models.CharField(max_length=200)
	size = models.ForeignKey(Size, on_delete=models.CASCADE)
	color = models.ForeignKey(Color, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('title',)


############################################
# This is a table to hold the Order
############################################
class Order(models.Model):
	widgets = models.ManyToManyField(Widget, through='WidgetOrder')

	def __str__(self):
		return str(self.id)


############################################
# This is a through table to hold all of the widgets and their quantities to an order
############################################
class WidgetOrder(models.Model):
	widget = models.ForeignKey(Widget, on_delete=models.CASCADE)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField()

	def __str__(self):
		return str(self.id)
