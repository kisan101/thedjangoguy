from djang.contrib.auth import get_user_model
from django.db import models


class Author(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	author_name = CharField()

	def __str__(self):
		return self.user.username


class Post(models.Model):
	title = models.CharField(max_length=100)
	overview = models.TextField()
	author = models.ForeginKey(Author,on_delete=models.CASCADE)

