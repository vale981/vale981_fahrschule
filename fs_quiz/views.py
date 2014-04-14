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

    height=75*Frage.objects.count()
    height_menu = height + 10
    if Frage.objects.count() == 0:
        height = 170
        height_menu = height

    len_quiz = len(Quiz.objects.get(id=quiz_id).title)
    count=Frage.objects.filter(quiz=quiz_id).count
    count_aw = 0
    aw = Frage.objects.filter(quiz=quiz_id)

    cs.update({'quiz': Quiz.objects.get(id=quiz_id),
                             'Frage': Frage.objects.all(),
                             'len': len_quiz,
                             'hg': height,
                             'hg_m': height_menu,
                             'user': request.user,
                             'aw': Antwort.objects.all(),
                             'count': count,
                             'count_aw': count_aw})
    return render_to_response('quiz.html', cs)

def check_view(request):

        user_id = request.POST.get('user_log', '')
        user_act = User.objects.get(id=user_id)
        quiz_id = request.POST.get('quiz', '')
        quiz = Quiz.objects.get(id=quiz_id)
        frage_list = Frage.objects.all()
        for frage_list in quiz.fragen.all():
            frage = frage_list
            aw_list = Antwort.objects.all()
            for aw_list in frage.antworten.all():
                antwort = aw_list
                aw_id = antwort.id
                richtig = antwort.richtig
                check = request.POST.get('aw_check'+str(aw_id), '')
                if bool(check) == bool(richtig):
                    richtig_send = True
                else:
                    richtig_send = False

                res = Results(quiz=quiz, frage=frage, user=user_act, richtig=richtig_send, choice=check, aw=antwort)
                res.save()
        return  HttpResponseRedirect('/quiz/all/')


