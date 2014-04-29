from django.db import models
from django.contrib.auth.models import User
import datetime
class Antwort(models.Model):


    content = models.CharField(max_length=1000,
                               blank=False,
                               help_text="Text der Antwort",
                               verbose_name='Antwort Text',
                               )

    richtig = models.BooleanField(blank=True)

    bild = models.ImageField(upload_to='pics/', blank=True, verbose_name="Antwort Bild")

    def __unicode__(self):
        return self.content
    def __str__(self):              # __unicode__ on Python 2
        return self.content



    class Admin:
        pass
    class Meta:
        verbose_name_plural='Antworten'

class Frage(models.Model):


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
    class Meta:
        verbose_name_plural='Fragen'

class Quiz(models.Model) :
    fragen = models.ManyToManyField(Frage, blank=True, verbose_name="Fragen")

    title = models.CharField(max_length=60,
                             blank=False,
                             verbose_name="Titel"
                             )

    description = models.TextField(blank=True,
                                   help_text="Die Beschreibung des Quiz",
                                   verbose_name="Beschreibung"
                                   )
    color = models.CharField(blank=True, max_length=23)
    class Admin:
        pass

    def __unicode__(self):
        return self.title
    def __str__(self):              # __unicode__ on Python 2
        return self.title

    class Meta:
        verbose_name_plural='Quiz'

class Results(models.Model):
    quiz=models.ForeignKey(Quiz, blank=True, )
    frage=models.ForeignKey(Frage, blank=True, )
    user=models.ForeignKey(User, blank=True, )
    richtig = models.BooleanField(blank=True)
    aw = models.ForeignKey(Antwort)
    choice = models.BooleanField(blank=True)
    datetime = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        # sort by "the date" in descending order unless
        # overridden in the query with order_by()
        ordering = ['-datetime']