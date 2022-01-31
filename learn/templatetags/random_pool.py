import random
from django import template
from ..models import WordPool

register = template.Library()

@register.simple_tag(takes_context=True)
def random_question(context):
    request = context['request']
    print('User id : ', request.user.id)
    Database = set(WordPool.objects.filter(user=request.user.id))

    word_list = random.sample(Database, 3) # get 3 options for question
    question = random.sample(word_list, 1) # set question
    options = [word_list[x].word for x in range(len(word_list))] # Set options for quiz
    language = question[0].language # set language
    answer = question[0].word # set true answer

    return question[0].original_text, options, language, answer