from django.db import models

# Create your models here.

class Size(models.Model):
	size = models.CharField(max_length=25)

	def __str__(self):
		return self.size


class Color(models.Model):
	color = models.CharField(max_length=25)

	def __str__(self):
		return self.color


class Widget(models.Model):
	title = models.CharField(max_length=200)
	size = models.ForeignKey(Size, on_delete=models.CASCADE)
	color = models.ForeignKey(Color, on_delete=models.CASCADE)
	inventory_number = models.PositiveIntegerField(default=0, null=True, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('title',)


class Order(models.Model):
	widgets = models.ManyToManyField(Widget, through='WidgetOrder')

	def __str__(self):
		return str(self.id)


class WidgetOrder(models.Model):
	widget = models.ForeignKey(Widget, on_delete=models.CASCADE)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField()

	def __str__(self):
		return str(self.id)
