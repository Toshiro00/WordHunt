from django.contrib import admin
from .models import WordPool, AnsweredPool
# Register your models here.
admin.site.register(WordPool)
admin.site.register(AnsweredPool)