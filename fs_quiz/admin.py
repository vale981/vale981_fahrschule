from django.contrib import admin

# Register your models here.
from fs_quiz.models import *
admin.site.register(Frage)
admin.site.register(Quiz)
admin.site.register(Antwort)

from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

from userprofile.models import UserQuizRel

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserQuizRelInline(admin.StackedInline):
    model = UserQuizRel
    can_delete = False
    verbose_name_plural = 'Quiz Verwaltung'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserQuizRelInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
