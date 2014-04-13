from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model) :
    title = models.CharField(max_length=60,
                             blank=False,
                             verbose_name="Titel"
                             )

    description = models.TextField(blank=True,
                                   help_text="Die Beschreibung des Quiz",
                                   verbose_name="Beschreibung"
                                   )
    class Admin:
        pass

    def __unicode__(self):
        return self.title
    def __str__(self):              # __unicode__ on Python 2
        return self.title








class Antwort(models.Model):


    content = models.CharField(max_length=1000,
                               blank=False,
                               help_text="Text der Antwort",
                               verbose_name='Antwort Text',
                               )

    richtig = models.BooleanField(blank=True)

    def __unicode__(self):
        return self.content
    def __str__(self):              # __unicode__ on Python 2
        return self.content



    class Admin:
        pass


class Frage(models.Model):

    quiz = models.ManyToManyField(Quiz, blank=True, )

    content = models.CharField(max_length=1000,
                               blank=False,
                               verbose_name='Frage Text',
                               )
    antworten = models.ManyToManyField(Antwort, blank=False, verbose_name='Antworten' )

    class Admin:
        pass

    def __unicode__(self):
        return self.content
    def __str__(self):              # __unicode__ on Python 2
        return self.content

class Results(models.Model):
    quiz=models.ForeignKey(Quiz, blank=True, )
    frage=models.ForeignKey(Frage, blank=True, )
    user=models.ForeignKey(User, blank=True, )
    richtig = models.BooleanField(blank=True)
    aw = models.ForeignKey(Antwort)
    choice = models.BooleanField(blank=True)

