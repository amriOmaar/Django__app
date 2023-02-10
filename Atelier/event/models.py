from django.db import models
from django.utils import timezone
from datetime import datetime
from person.models import Person
from django.core.exceptions import ValidationError

def is_date_event(value):
    if value <= timezone.now():
        raise ValidationError(
        'event date sup')
    return value

class Event(models.Model):

    category_list = (
        ("Musique", "Musique"),
        ("Sport", "Sport"),
        ("Cinema", "Cinema")
    )



    title = models.CharField(max_length=30) 
    description = models.TextField()
    image = models.ImageField()
    category = models.CharField(max_length=20, choices=category_list)
    state = models.BooleanField(default=False)
    nbe_participant = models.IntegerField(default=0)
    evt_date = models.DateTimeField(blank=True) #validators=[is_date_event]
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    organisateur = models.ForeignKey(
        Person, on_delete=models.SET_NULL, blank=True, null=True
    )
    participant = models.ManyToManyField(
        Person, through = 'participant', blank=True, null=True
    )



    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(
                    evt_date__gte=datetime.now()
                ),
                name='please check out the even date'
            ), 
        ]


class participants(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    evenement = models.ForeignKey(Event, on_delete=models.CASCADE)
    date_participation = models.DateTimeField(default=datetime.now)

    class Meta:
        unique_together = [['person', 'evenement']]
