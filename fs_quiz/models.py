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

class Frage(models.Model):

    quiz = models.ManyToManyField(Quiz, blank=True, )

    content = models.CharField(max_length=1000,
                               blank=False,
                               verbose_name='Frage Text',
                               )





    class Admin:
        pass

    def __unicode__(self):
        return self.content
    def __str__(self):              # __unicode__ on Python 2
        return self.content

class Antwort(models.Model):
    frage = models.ManyToManyField(Frage, blank=False, )

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

    def get_related_to(self, status):
        return self.related_to.filter(
        from_people__status=status,
        from_people__to_person=self)

    class Admin:
        pass




class Results:
    quiz=models.ManyToManyField(Quiz, blank=True, )
    frage=models.ManyToManyField(User, blank=True, )
    user=models.ManyToManyField(User, blank=True, )
    richtig = models.BooleanField(blank=True)
    choice = models.ManyToManyField(Antwort)