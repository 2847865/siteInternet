from django.db import models

# Create your models here.
class Page(models.Model):
	page_name = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')
	header = models.CharField(max_length=500)
	nav = models.CharField(max_length=500)
	section = models.CharField(max_length=50000)
	footer = models.CharField(max_length=500)
	def __unicode__(self):
		return self.page_name