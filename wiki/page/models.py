from django.db import models

# Create your models here.
class Page(models.Model):
	name = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')
	header = models.CharField(max_length=500)
	nav1 = models.CharField(max_length=500)
	nav2 = models.CharField(max_length=500)
	nav3 = models.CharField(max_length=500)
	image = models.ImageField(blank=False, upload_to='media/')
	section = models.CharField(max_length=5000)
	footer1 = models.CharField(max_length=500)
	footer2 = models.CharField(max_length=500)
	footer3 = models.CharField(max_length=500)
	
	def __unicode__(self):
		return self.name