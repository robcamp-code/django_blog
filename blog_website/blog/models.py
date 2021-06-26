from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now) #auto_now_add creates a now datetime but it can't be updated
	author = models.ForeignKey(User, on_delete=models.CASCADE) # if a post is deleted so is the author. (one way steet)

	def __str__(self):
		return self.title
