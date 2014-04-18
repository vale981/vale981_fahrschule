from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^all/', 'fs_quiz.views.quizes', name='home'),
    url(r'^get/(?P<quiz_id>\d+)$', 'fs_quiz.views.quiz', name='home'),
    url(r'^check/', 'fs_quiz.views.check_view', name='check'),
    url(r'^auswertung/', 'fs_quiz.views.auswertung_index', name='Auswertung'),
    url(r'^aw/get/(?P<user_id>\d+)$', 'fs_quiz.views.ausw_user', name='awuser'),
    url(r'^aw/get/(?P<user_id>\d+)/(?P<quiz_id>\d+)$', 'fs_quiz.views.ausw_user_quiz', name='awuserquiz'),
)
