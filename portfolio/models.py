from django.db import models

# Create your models here.
class Site(models.Model):
	site_image = models.ImageField(upload_to='post_images/')
	site_title = models.CharField(max_length=300)
	site_text = models.TextField()
	site_link = models.TextField()