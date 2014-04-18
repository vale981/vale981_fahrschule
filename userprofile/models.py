from django.db import models
from django.contrib.auth.models import User
from fs_quiz.models import Quiz, Results
import datetime

def get_def():
    return Quiz.objects.all()

class UserQuizRel(models.Model):
    quiz=models.ManyToManyField(Quiz, blank=True, related_name='User', verbose_name='abgeschlossene Quizs')
    allowed_quiz=models.ManyToManyField(Quiz, blank=True, related_name='User-get', verbose_name='Erlaubte Quizs', default=get_def())
    user=models.OneToOneField(User)

class ResultGroup(models.Model):
    user = models.ForeignKey(User)
    results = models.ManyToManyField(Results, blank=True)
    res_time = models.DateTimeField(default=datetime.datetime.now())
    quiz = models.ForeignKey(Quiz)


