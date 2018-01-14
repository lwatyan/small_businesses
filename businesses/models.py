from django.db import models

# Create your models here.
class Business(models.Model):
	name 	= models.CharField(max_length=255)
	description = models.TextField()
	established = models.DateTimeField()
	
