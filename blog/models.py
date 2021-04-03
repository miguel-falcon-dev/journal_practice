from django.db import models

# Create your models here.
class Entry (models.Model):
    creation_date = models.DateField(('creation_date'), auto_now=False, auto_now_add=False, blank=False)

    updated_date = models.DateTimeField(('updated_date'), auto_now=True, blank = True)

    class FeelingOptions(models.TextChoices):
        HAPPY = 'HA'
        SAD = 'SA'
        ANGRY = 'AN'
        CONFIDENT = 'CO'
        SICK = 'SI'
        AMAZED = 'AM'
    
    feeling = models.CharField('feeling', max_length=2, choices=FeelingOptions.choices)

    description = models.TextField('description')

    photo = models.ImageField(null=True)

    time_stamp = models.DateTimeField(('time_stamp'), auto_now=False, auto_now_add=True, blank=False)

    

class Practice (models.Model):
    text_part = models.TextField('text')
    date_part = models.DateField(('date'), auto_now=False, auto_now_add=False)