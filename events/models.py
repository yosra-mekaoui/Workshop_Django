from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from users.models import *
from datetime import datetime
# Create your models here.

def titleValidator(value):
    if not value.istitle():
        raise ValidationError(
           "Title must contain capital letters"
        )
def dateValidator(value):
    if value < datetime.now().date():
        raise ValidationError(
           "insert now date please"
        ) 
      
class Event(models.Model):
    CATEGORY_CHOICES = (
        ('Music', 'Music'),
        ('Cinema', 'Cinema'),
        ('Sport', 'Sport'),
    )

    title = models.CharField(max_length=255, null=True, validators=[titleValidator])
    description = models.TextField()
    eventImage = models.ImageField(upload_to='images/', blank=True)

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=8)
    state = models.BooleanField(default=False)

    nbrParticipants = models.IntegerField(default=0, validators=[
        MinValueValidator(limit_value=0, message='Number of participants must be a postive')
    ])
    eventDate = models.DateField(validators=[dateValidator])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 3mlna relation bin user wl event bl organiser
    organizer = models.ForeignKey(Person, on_delete=models.CASCADE)



    # bch naamlou relation many to many bin user wl event , el relation saminha participate
    # through hya el classe el intermediaire chnya esmhaa 
    participte = models.ManyToManyField(
        Person,
        related_name="participations",
        through='Participation'
    )
    def __str__(self):
        return self.title

class Participation(models.Model):
    person = models.ForeignKey(Person,
         on_delete=models.CASCADE) 
    event = models.ForeignKey(Event,
         on_delete=models.CASCADE)    
    datePart = models.DateField(auto_now=True)   
# nhbou na3tiw des information 3al classe hya bidhaa
    class Meta:
        unique_together = ('person','event')
