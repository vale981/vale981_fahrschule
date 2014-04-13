from django.contrib import admin

# Register your models here.
from fs_quiz.models import *
admin.site.register(Frage)
admin.site.register(Quiz)
admin.site.register(Antwort)