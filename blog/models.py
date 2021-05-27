from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os
import datetime

# https://stackoverflow.com/questions/28166784/restricting-access-to-private-file-downloads-in-django
# по ідеї захист від завантаження по url виконує сам http сервер, знайшов тільки як реалізувати на apache)
class Post(models.Model):
	title = models.CharField(max_length=100)
	file = models.FileField(null=True,blank=True,upload_to='Files')
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	accessability = models.BooleanField(default=True) # https://www.ordinarycoders.com/blog/article/using-django-form-fields-and-widgets
	#day = models.DateField(initial=datetime.date.today)

	def __str__(self):
		return self.title

	def extension(self):
		name, extension = os.path.splitext(self.file.name)
		return extension

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

        
