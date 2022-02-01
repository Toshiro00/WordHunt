from django import template
from django.db.models import Q
from ..models import WordPool
import random
from ..translate import translate_text

register = template.Library()


@register.simple_tag(takes_context=True)
def new_word(context):
    request = context['request']

    new_word_list = []
    turkish = ''
    new_word = ''

    # Read word list
    with open('./learn/static/learn/words.txt', 'r') as file:
        words = file.readlines()
    
    # Remove newline characters from every word
    for w in words:
        new_word_list.append(w.rstrip())
    
    # Get list of database
    wordpool = WordPool.objects.filter(user=request.user.id).all()

    if len(wordpool) > 0:    
        for word in wordpool:
            # If word already in database remove from list            
            if word.original_text.rstrip() in new_word_list:
                new_word_list.remove(word.original_text.rstrip())
            else:
                # Select one sample from words
                new_word = random.sample(new_word_list, 1)
                new_word = new_word[0].title()
            
        # Translate selected sample 
        translated_word = translate_text('en', 'tr', new_word)
        turkish = translated_word.json()['responseData']['translatedText']
    else:
        # Select one sample from words
        new_word = random.sample(new_word_list, 1)
        new_word = new_word[0].title()
            
        # Translate selected sample 
        translated_word = translate_text('en', 'tr', new_word)
        turkish = translated_word.json()['responseData']['translatedText']

    return turkish.title(), new_word.title()