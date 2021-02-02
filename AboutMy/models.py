from django.db import models


# Create your models here.
class Posts(models.Model):
    post_image = models.ImageField(upload_to='post_images/')
    post_text = models.CharField(max_length=300)
