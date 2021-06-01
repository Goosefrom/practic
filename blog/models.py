from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os
import datetime
from django.core.exceptions import ValidationError

# https://stackoverflow.com/questions/28166784/restricting-access-to-private-file-downloads-in-django
# по ідеї захист від завантаження по url виконує сам http сервер, знайшов тільки як реалізувати на apache)

def file_size(value): # file size checker
    limit = 50 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 50 MiB.') #https://i.ytimg.com/vi/OTA7Z00NeAY/hqdefault.jpg

class Post(models.Model):
	title = models.CharField(max_length=100)
	file = models.FileField(null=False,blank=False,upload_to='Files',validators=[file_size])
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
