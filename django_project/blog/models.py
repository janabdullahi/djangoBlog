from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Permission, User

class Post(models.Model):
   title = models.CharField(max_length=20, help_text='Enter title')
   content = models.TextField()
   date_posted = models.DateTimeField(default=timezone.now)
   author = models.ForeignKey(User, on_delete=models.CASCADE)

   def __str__(self):
      return self.title
