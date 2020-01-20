from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
    link_text = models.CharField(max_length=200)
    author = models.ForeignKey(User, default=None,blank=True, on_delete=models.PROTECT, null = True)
    firstChar = models.CharField(max_length=1, blank=True, null=True)
    def __str__(self):
        return self.link_text
# Create your models here.
