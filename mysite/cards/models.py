from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cards(models.Model):

	owner = models.ForeignKey(User)
	url=models.URLField()
	name=models.CharField(max_length=60)
	image=models.ImageField(upload_to='Pictures')
	media_type=models.CharField(max_length=32)
	create_at=models.DateTimeField('date published')
    
	def __str__(self):
		return self.name