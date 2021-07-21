from django.db import models
#from random import randint

# Create y"our models" here.

"""class Roll(models.Model):
    def roll_dice(self):
        result = 0
        rolled_numbers = []
        for n in range(Choice.number_of_dice):
            number = randint(1, Choice.dice_walls + 1)
            rolled_numbers.append(number)
            result += number
    def __str__(self):
        return str(self.result)"""
            
class Choice(models.Model):
    POSSIBLE_DICE_WALL_NUMBERS = (
        (2,'2'),(3,'3'),(4,'4'),(6,'6'),(8,'8'),(10,'10'),(12,'12'),(20,'20'),(100,'100'),
        )
    number_of_dice = models.PositiveSmallIntegerField
    number_of_dice.max_value = 20
    dice_walls = models.PositiveIntegerField(choices=POSSIBLE_DICE_WALL_NUMBERS)
    
            