from django import forms
from .models import WordPool, AnsweredPool
from .templatetags.random_pool import random_question
import random

class TranslateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['word'].required = False

    
    class Meta:
        model = WordPool
        fields = ['word']
        widgets = {
            'word': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            )
        }
        labels = {
            'word': ''
        }
    
class WordPoolForm(forms.ModelForm):
    class Meta:
        model = AnsweredPool
        fields = [] # Just show answers

class NewWordForm(forms.ModelForm):
    class Meta:
        model = WordPool
        fields = []