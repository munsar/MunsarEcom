from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BlogCategory(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class BlogPost(models.Model):
	author = models.CharField(max_length=50)
#	category = models.ForeignKey(BlogCategory, related_name='cat', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	publish_date = models.DateField()
	publish = models.BooleanField(default=False)
	file = models.FileField(null=True, blank=True, upload_to='Blog_post/File/%Y/%M')
	image = models.ImageField(upload_to='Blog_post/Image/%Y/%m/%d')

	def __str__(self):
		return self.title

