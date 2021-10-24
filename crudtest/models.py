from django.db import models

# Create your models here.

class crudtest(models.Model):
	text = models.CharField(max_length=100)

	def __dtr__(self):
		return self.text
