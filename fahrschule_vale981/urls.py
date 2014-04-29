from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Examples:
    (r'^quiz/', include('fs_quiz.urls')),
    # url(r'^blog/', include('blog.urls')),
    (r'^$', 'fahrschule_vale981.views.login'),
    (r'^login/', 'fahrschule_vale981.views.login'),
    (r'^logout/', 'fahrschule_vale981.views.logout_view'),
    (r'^auth/', 'fahrschule_vale981.views.auth_view'),
    (r'^fehler/', 'fahrschule_vale981.views.error'),

    url(r'^admin/', include(admin.site.urls)),
)
from django.conf import settings

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

