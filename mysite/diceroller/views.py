#from django.shortcuts import render
from django.views import generic
from .models import Choice, Results
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
    model = Results 
    template_name = 'diceroller/results.html'
    
    
"""def initial(request):
    choice = Choice 
    aroll = ForeignKey(roll)
    return render(request, 'diceroller/initial.html',{'choice':choice})
    
def results(request):
#    model = Roll
    return render(request, 'diceroller/results.html',{'roll':roll})"""
    
def roll(request):
    if Choice.objects.all().exists():
        choice_id=Choice.objects.latest('id').id + 1
    else:
        choice_id = 1
    choice = Choice(pk=choice_id)
    choice.save()
    result = choice.results_set.create(result=0)
    print(choice.number_of_dice)
    print(choice.dice_walls)
    #rolled_number_pk=1
    for i in range(choice.number_of_dice):
        number = randint(1, choice.dice_walls)
        result.result += number
        #result.RolledNumber(pk=rolled_number_pk).post(number)
        result.rolled_numbers.append(number)
        result.save()
    return HttpResponseRedirect(reverse('diceroller:results', args = (choice.id,)))
    
