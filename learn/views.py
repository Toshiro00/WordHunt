from django.shortcuts import render, redirect
from .forms import TranslateForm, WordPoolForm, NewWordForm
from .models import *
from .translate import translate_text
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .templatetags.wrong_answers import wrong_answer
from django.template import RequestContext
from pathlib import Path


# Create your views here.
@login_required()
def translate_page(request):
    text = ''
    
    BASE_DIR = Path(__file__).resolve().parent.parent
    print(BASE_DIR)

    if request.method == 'POST':
        form = TranslateForm(request.POST)
        if form.is_valid():
            # Get language from radio button
            language = request.POST.get('language')

            # Create variable for save data as logged user
            saver = form.save(commit=False)


            # Get user input
            text = form.cleaned_data.get('word')

            if text == '':
                messages.add_message(request, messages.ERROR, 'Input can not be null')
            else:
                # Check language
                if language == '[TR-EN]':
                    text = translate_text('tr', 'en',  text)
                elif language == '[EN-TR]':
                    text = translate_text('en', 'tr', text)
                else:
                    raise form.errors

                # Get translated value from API
                text = text.json()['responseData']['translatedText']

                # Save as logged user
                saver.user = request.user
                saver.word = text.title()
                saver.language = language
                saver.original_text = form.cleaned_data.get('word').title()
                saver.save()
                
                # Success
                messages.add_message(request, messages.SUCCESS, 'Word saved to database.')
        else:
            print(form.errors)
    else:
        form = TranslateForm()
            
    return render(request, 'learn/translate_page.html', {'form': form, 'text':text})

@login_required()
def word_pool_quiz(request):
    # Translate 'question' for checking answer
    data = WordPool.objects.values_list()
    if len(data) > 5:
        if request.method == "POST":
            form = WordPoolForm(request.POST)
            saver = form.save(commit=False)
            saver.user = request.user

            question = request.POST.get('question')
            language = request.POST.get('language')
            translated_question = translate_text('en', 'tr', question)
            translated_question = translated_question.json()['responseData']['translatedText']

            # Get option from user
            option = request.POST.get('option')

            # Set answer variable
            answer = request.POST.get('answer')

            # Check answer
            if option == None:
                messages.add_message(request, messages.ERROR, 'Birşeyler seçmek zorundasın')    # If answer is none show error to user
            elif option == answer:
                saver.question = question
                saver.result = 1
                saver.answer = answer
                saver.language = language
                saver.save()
                messages.add_message(request, messages.SUCCESS, 'Doğru cevap! Böyle devam et')        # If answer is true show success to user
            elif option != answer:
                saver.question = question
                saver.result = 0
                saver.answer = answer
                saver.language = language
                saver.save()
                messages.add_message(request, messages.INFO, "Üzgünüm :( Doğru cevap " + answer)     # If answer is wrong show answer to user and send question to 'FailPool'


        return render(request, 'learn/word_pool_quiz.html')
    else:
        return HttpResponseNotFound('Veritabanında yeterli kelime bulunmadığından bu sayfaya erişim sağlamayazsınız. Lütfen en az 6 çeviri yaparak kelime havuzunu doldurun.')

@login_required()
def word_pool(request):
    data_tr_en = []
    data_en_tr = []

    # Create word pool table
    for d in WordPool.objects.filter(user=request.user.id):
        if d.language == '[TR-EN]':
            data_tr_en.append([d.word, d.original_text])
        elif d.language == '[EN-TR]':
            data_en_tr.append([d.word, d.original_text])

    return render(request, 'learn/word_pool.html', {'data_tr_en': data_tr_en, 'data_en_tr': data_en_tr})

@login_required()
def new_word(request):


    # Set translation direction
    language = '[EN-TR]'

    form = TranslateForm(request.POST)

    if request.method == 'POST':
        english = request.POST.get('english')
        turkish = request.POST.get('turkish')

        # Set variable for save data as logged user
        #if form.is_valid():
        saver = form.save(commit=False)

        # Save as logged user
        saver.user = request.user
        saver.word = turkish.title()
        saver.language = language
        saver.original_text = english.title()
        saver.save()

        # Success
        messages.add_message(request, messages.SUCCESS, 'Kelime veritabanına kaydedildi.')

    return render(request, 'learn/new_word.html', {'form': form})

@login_required()
def wrong_answers(request):
    #q, _, _ = wrong_answer()

    if request.method == 'POST':
        form = WordPoolForm(request.POST)
        if form.is_valid():
            
            # Get and set answers
            get_answer = request.POST.get('answer')
            org_answer = request.POST.get('org_answer')
            question_id = request.POST.get('question_id')

            # Get desired db record for update
            try:
                db_record = AnsweredPool.objects.get(pk=int(question_id), user=request.user.id)

                # Check answer
                if get_answer == org_answer:
                    db_record.result = 1
                    db_record.save()
                    messages.add_message(request, messages.SUCCESS, 'Cevabın doğru!')
                elif get_answer == None:
                    messages.add_message(request, messages.ERROR, 'Birşeyler yazmalısın')
                else:
                    messages.add_message(request, messages.INFO, 'Üzgünüm :( Doğru cevap ' + org_answer)
            except:
                print('Record not found.')

    return render(request, 'learn/wrong_answers.html')

