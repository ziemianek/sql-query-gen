from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.TextField()
    query = models.TextField()
    generated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['generated_on']
