from django.db import models
from django.contrib.auth.models import AbstractUser


def is_mail_esprit(value):
    if str(value).endswith('@esprit.tn') == False:
        raise ValidationError(
            f"Your mail - {value} - must be @esprit"
        )
    return value

def is_cin_length(value):
    if len(value) != 8:
        raise ValidationError("your cin must have 8 characters")
    return value



# Create your models here.
class Person(AbstractUser):
    cin = models.CharField(primary_key=True, max_length=8, validators=[is_mail_esprit])
    username = models.CharField("Username", max_length=50, unique=True, validators=[is_cin_length])
    email = models.EmailField("Email", unique=True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural="Personne"
    
