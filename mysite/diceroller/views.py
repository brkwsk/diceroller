from django.shortcuts import render
from django.views import generic
from .models import Choice
from random import randint

# Create your views here.

class InitialView(generic.ListView):
    model = Choice
    template_name = 'diceroller/initial.html'
    def get_queryset(self):
        return Choice.objects.all()
    
class ResultsView(generic.ListView):
#    model = Roll 
    template_name = 'diceroller/results.html'
    def get_queryset(self):
        return Choice.objects.all()
    
def roll(request):
    choice = Choice
    result = 0
    rolled_numbers = []
    for i in range(choice.number_of_dice):
        number = randint(1, choice.dice_walls)
        result += number
        rolled_numbers.append(number)
        result.save()
        rolled_numbers.save()
    
