from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Examples:
    (r'^quiz/', include('fs_quiz.urls')),
    # url(r'^blog/', include('blog.urls')),
    (r'^login/', 'fahrschule_vale981.views.login'),
    (r'^logout/', 'fahrschule_vale981.views.logout_view'),
    (r'^auth/', 'fahrschule_vale981.views.auth_view'),
    (r'^fehler/', 'fahrschule_vale981.views.error'),

    url(r'^admin/', include(admin.site.urls)),
)
