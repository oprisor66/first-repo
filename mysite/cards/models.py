from django.db import models

# Create your models here.
class Cards(models.Model):
	url=models.URLField()
	name=models.CharField(max_length=60)
	image=models.ImageField()
	media_type=models.CharField(max_length=32)
	create_at=models.DateTimeField('date published')