from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
#from django.template.loader import get_template
#from django.template import Context
#from django.views.generic.base import TemplateView
from django.core.context_processors import csrf
from fs_quiz.models import *
from fs_quiz.forms import *
from fs_quiz.forms import Results
from django.forms.models import modelformset_factory
from django.contrib import auth


def quizes(request):
    height=75*Quiz.objects.count()
    height_menu = height + 10
    if Quiz.objects.count() == 0:
        height = 170
        height_menu = height
    return render_to_response('quizzes.html',
                             {'quizes': Quiz.objects.all(),
                              'hg': height,
                              'hg_m': height_menu,
                              'user': request.user})

def quiz(request, quiz_id=1):
    cs = {}
    cs.update(csrf(request))

    # AuthorFormSet = modelformset_factory(Results, form=ResultForm)
    # if request.method == 'POST':
    #     formset = AuthorFormSet(request.POST, request.FILES)
    #     if formset.is_valid():
    #         formset.save()
    #         # do something.
    # else:
    #     formset = AuthorFormSet(queryset=Frage.objects.filter(quiz=quiz_id))

    height=75*Frage.objects.count()
    height_menu = height + 10
    if Frage.objects.count() == 0:
        height = 170
        height_menu = height

    len_quiz = len(Quiz.objects.get(id=quiz_id).title)
    cs.update({'quiz': Quiz.objects.get(id=quiz_id),
                             'Frage': Frage.objects.filter(quiz=quiz_id),
                             'len': len_quiz,
                             'hg': height,
                             'hg_m': height_menu,
                             'user': request.user,
                             'aw': Antwort.objects.all()})
    return render_to_response('quiz.html', cs)

def check_view(request):
    check = request.POST.get('aw_check', '')
    user = request.POST.get('user_log', '')
    frage = request.POST.get('frage', '')
    antwort = request.POST.get('antwort', '')
    richtig = request.POST.get('richtig', '')
    quiz_get = request.POST.get('quiz', '')
    res = Results(quiz=quiz_get, frage=frage, user=user, richtig=richtig, choice=check)
    res.save()
    return  HttpResponseRedirect('/quiz/all/')


