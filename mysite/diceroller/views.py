from django.shortcuts import render
from django.views import generic
from .models import Choice
from random import randint
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here".

class InitialView(generic.ListView):
    model = Choice
    template_name = 'diceroller/initial.html'
    def get_queryset(self):
        return Choice.objects.all()
    
class ResultsView(generic.DetailView):
    model = Choice
    template_name = 'diceroller/results.html'
    
def home(request):
    return HttpResponseRedirect(reverse('diceroller:initial'))

def roll(request):
    if Choice.objects.all().exists():
        choice_id=Choice.objects.latest('id').id + 1
    else:
        choice_id = 1
        
    choice = Choice(pk=choice_id)
    choice.clean()
    choice.dice_walls = int(request.POST['dice_walls'])
    choice.number_of_dice = int(request.POST['number_of_dice'])
    
    #if choice.dice_walls <2:
    if choice.dice_walls not in choice.dice_wall_numbers:
        choice.delete()
        return render(request, 'diceroller/initial.html', {"error_message":"Choose one of the available dice types."})
    if choice.number_of_dice < 1:
        choice.delete()
        return render(request, 'diceroller/initial.html', {"error_message":"Choose a positive number of dice."})
    choice.save()
    
    result = choice.results_set.create(result=0)
    
    for i in range(choice.number_of_dice):
        number = randint(1, choice.dice_walls)
        result.result += number
        result.rollednumber_set.create(value=number)
        result.save()
        
    return HttpResponseRedirect(reverse('diceroller:results', args = (choice.id,)))
    
