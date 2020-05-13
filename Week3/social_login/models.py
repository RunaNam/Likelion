from django.db import models
from imagekit.models import ImageSpecField
from imgagekit.processors import ResizeToFill

# Create your models here.

class Pictures (models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to = "blogimg")
    image_thumbnail = ImageSpecField(source = 'image', processors = [ResizeToFill(120, 100 )])