from django.db import models
from django.forms import ModelForm

# Create your models here.

# Model for sine of a number


class Input(models.Model):
    r = models.FloatField()


class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ('r',)

# Model for addition of two numbers


class Addition(models.Model):
    a = models.FloatField()
    b = models.FloatField()


class AdditionForm(ModelForm):
    class Meta:
        model = Addition
        fields = ('a', 'b',)
