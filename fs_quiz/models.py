from django.db import models

# Create your models here.
class Quiz(models.Model) :
    title = models.CharField(max_length=60,
                             blank=False,
                             )

    description = models.TextField(blank=True,
                                   help_text="a description of the quiz",
                                   )
    class Admin:
        pass

    def __unicode__(self):
        return self.title

class Frage(models.Model):

    quiz = models.ManyToManyField(Quiz, blank=True, )

    content = models.CharField(max_length=1000,
                               blank=False,
                               help_text="Enter the question text that you want displayed",
                               verbose_name='Question',
                               )


    class Admin:
        pass

    def __unicode__(self):
        return self.content

