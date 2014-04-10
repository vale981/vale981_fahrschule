from django.shortcuts import render_to_response
#from django.http import HttpResponse
#from django.template.loader import get_template
#from django.template import Context
#from django.views.generic.base import TemplateView
from fs_quiz.models import *


def quizes(request):
    height=75*Quiz.objects.count()
    height_menu = height + 10
    if Quiz.objects.count() == 0:
        height = 170
        height_menu = height
    return render_to_response('quizzes.html',
                             {'quizes': Quiz.objects.all(),
                              'hg': height,
                              'hg_m': height_menu})

def quiz(request, quiz_id=1):

    height=75*Frage.objects.count()
    height_menu = height + 10
    if Frage.objects.count() == 0:
        height = 170
        height_menu = height

    len_quiz = len(Quiz.objects.get(id=quiz_id).title)

    return render_to_response('quiz.html',
                             {'quiz': Quiz.objects.get(id=quiz_id),
                             'Frage': Frage.objects.filter(quiz=quiz_id),
                             'len': len_quiz,
                             'hg': height,
                             'hg_m': height_menu})

