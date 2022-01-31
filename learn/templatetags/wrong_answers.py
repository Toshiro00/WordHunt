import random
from django import template
from ..models import AnsweredPool

register = template.Library()



@register.simple_tag(takes_context=True)
def wrong_answer(context):
    request = context['request']
    data = AnsweredPool.objects.filter(user=request.user.id)

    question = []
    answer = []
    question_id = 0

    for d in data:
        if d.result == 0:
            question.append(d)

    if len(question) != 0:
        question = random.sample(question, 1)
        answer = question[0].answer
        question_id = question[0].id
        question = question[0].question

    return question, answer, question_id