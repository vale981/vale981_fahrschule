from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from userprofile.models import UserQuizRel
from fs_quiz.models import Quiz


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):

    firstname = request.POST.get('firstname', '')
    lastname = request.POST.get('lastname', '')
    password = 'standart'
    username = firstname + lastname
    User.objects.create_user(username=firstname+lastname, password='standart', first_name=firstname, last_name=lastname)

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        uqr = UserQuizRel(user=request.user)
        uqr.save()
        uqr.allowed_quiz = Quiz.objects.all()
        uqr.save()
        return  HttpResponseRedirect('/quiz/all/')
    else:
        return HttpResponseRedirect('/fehler/')

def error(request):
    return render_to_response('fehler.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')