from django.db import models
from random import randint

# Create your models here.

class Roll(models.Model):
    choice = ForeignKey(Choice, on_delete = models.CASCADE)
    number_of_dice = choice.number_of_dice
    dice_walls = choice.dice_walls
    def roll_dice(self):
        result = 0
        rolled_numbers = []
        for n in range(choice.number_of_dice):
            number = randint(1, choice.die_walls + 1)
            rolled_numbers.append(number)
            result += number
    def __str__(self):
        return str(result)
            
class Choice(models.Model):
    possible_dice_wall_numbers = [2,3,4,6,8,10,12,20,100]
    number_of_dice = models.PositiveIntegerField(max_value = 20)
    dice_walls = models.PositiveIntegerField(choices = possible_dice_wall_numbers)
    
            