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
from userprofile.models import UserQuizRel, ResultGroup


def quizes(request):
    height=75*Quiz.objects.count()
    height_menu = height + 10
    if Quiz.objects.count() == 0:
        height = 170
        height_menu = height
    if request.user.is_authenticated():
        user_quiz = UserQuizRel.objects.get(user=request.user)
    else:
        user_quiz = 0
    return render_to_response('quizzes.html',
                             {'quizes': Quiz.objects.all(),
                              'hg': height,
                              'hg_m': height_menu,
                              'user': request.user._wrapped if hasattr(request.user,'_wrapped') else request.user,
                              'user_quiz': user_quiz})

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
import  datetime
def check_view(request):

        user_id = request.POST.get('user_log', '')
        user_act = User.objects.get(id=user_id)

        quiz_id = request.POST.get('quiz', '')

        quiz = Quiz.objects.get(id=quiz_id)
        user_quiz = UserQuizRel.objects.get(user=user_act)
        user_quiz.quiz.add(quiz)
        user_quiz.allowed_quiz.remove(quiz)
        user_quiz.save()
        result_group=ResultGroup(user=user_act, quiz=quiz)
        result_group.res_time = datetime.datetime.now()
        result_group.save()

        frage_list = Frage.objects.all()
        for frage_list in quiz.fragen.all():
            frage = frage_list
            aw_list = Antwort.objects.all()
            for aw_list in frage.antworten.all():
                antwort = aw_list
                aw_id = antwort.id
                richtig = antwort.richtig
                check = request.POST.get('aw_check'+str(aw_id), '')
                if bool(richtig) == bool(check):
                    richtig=True
                else:
                    richtig=False

                res = Results(quiz=quiz, frage=frage, user=user_act, richtig=richtig, choice=check, aw=antwort)
                res.save()
                result_group.results.add(res)
                result_group.save()
        return  HttpResponseRedirect('/quiz/all/')

def auswertung_index(request):
    return render_to_response('auswertung.html', {'user': request.user,
                                                  'users': User.objects.all()})

def ausw_user(request, user_id=1):
    user = User.objects.get(id=user_id)
    return render_to_response('auswertung_user.html', {'user': user,
                                                 'results': Results.objects.filter(user=user),
                                                 'current_user': request.user,
                                                 'results_all': Results.objects.all(),
                                                 'fragen': Frage.objects.all(),
                                                 'quiz': Quiz.objects.all(),
                                                 'user_quiz': UserQuizRel.objects.get(user=user),
                                                 })
def ausw_user_quiz(request, user_id=1, quiz_id=1):
    user = User.objects.get(id=user_id)
    quiz = Quiz.objects.get(id=quiz_id)
    return render_to_response('auswertung_user_qzuiz.html', {'user': user,
                                                 'current_user': request.user,
                                                 'results': Results.objects.filter(user=user),
                                                 'results_all': Results.objects.all(),
                                                 'fragen': Frage.objects.all(),
                                                 'quiz': quiz,
                                                 'user_quiz': UserQuizRel.objects.get(user=user),
                                                 'result_group': ResultGroup.objects.filter(user=user, quiz=quiz),
                                                })
