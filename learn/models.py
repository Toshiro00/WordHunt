from django.db import models
from django.contrib.auth.models import User
import random

# Create your models here.
class WordPool(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.CharField(max_length=50, blank=False)
    language = models.CharField(max_length=10, default='')
    original_text = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.word

class AnsweredPool(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=50, default='')
    language = models.CharField(max_length=10, default='')
    answer = models.CharField(max_length=50)
    result = models.IntegerField(default=0)

    def __str__(self):
        return self.question


