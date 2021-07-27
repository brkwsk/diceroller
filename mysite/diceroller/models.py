from django.db import models
#from django.forms import ChoiceField
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
    #results = models.ForeignKey(Results, on_delete = models.CASCADE)
    POSSIBLE_DICE_WALL_NUMBERS = (
        (2,'2'),(3,'3'),(4,'4'),
        (6,'6'),(8,'8'),
        (10,'10'),(12,'12'),
        (20,'20'),(100,'100'),
        )
    number_of_dice = models.PositiveIntegerField(default=1)
    number_of_dice.max_value = 100
    dice_walls = models.PositiveIntegerField(choices=POSSIBLE_DICE_WALL_NUMBERS, default=6)
    def __str__(self):
        return "number of dice:{}, dice walls:{}".format(self.number_of_dice, self.dice_walls)
    
class Results(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    result = models.IntegerField()
    rolled_numbers = []
    def __str__(self):
        return str(self.result)
    
class RolledNumber(models.Model):
    value = models.IntegerField()
    result = models.ForeignKey(Results, on_delete=models.CASCADE)

"""class RolledNumber(models.Model):
    results = models.ForeignKey(Results, on_delete = models.CASCADE)
    number = models.IntegerField(default=0)
    def __str__(self):
        return str(self.number)"""
    
            