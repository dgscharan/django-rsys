from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    publish_date = models.DateField(null=True)



    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-details', args=(str(self.id)))
        