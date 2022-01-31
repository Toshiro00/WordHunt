from django.shortcuts import render
from learn.models import AnsweredPool, WordPool
from pathlib import Path
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def profile(request):
    total = len(WordPool.objects.filter(user=request.user.id))
    right_answers = len(AnsweredPool.objects.filter(user=request.user.id).filter(result=1))
    wrong_answers = len(AnsweredPool.objects.filter(user=request.user.id).filter(result=0))

    new_word_list = []

    # Read word list
    with open('./learn/static/learn/words.txt', 'r') as file:
        words = file.readlines()
    
    # Remove newline characters from every word
    for w in words:
        new_word_list.append(w.rstrip())
        
    # Get list of database
    wordpool = WordPool.objects.filter(user=request.user.id).all()
    
    for word in wordpool:            
        # If word already in database remove from list            
        if word.original_text.rstrip() in new_word_list:
            new_word_list.remove(word.original_text.rstrip())
   
    return render(request, 'user_profile/user_profile.html', {'total': total, 'right': right_answers, 'wrong': wrong_answers, 'new_words': len(new_word_list)})