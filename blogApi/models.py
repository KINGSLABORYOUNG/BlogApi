from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200 , blank=False)
    content = models.TextField(max_length=200, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return super().__str__()
