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

    organizer = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
