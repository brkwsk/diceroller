from django.db import models

# Create your models" here.

          
class Choice(models.Model):
    POSSIBLE_DICE_WALL_NUMBERS = (
        (2,'2'),(3,'3'),(4,'4'),
        (6,'6'),(8,'8'),
        (10,'10'),(12,'12'),
        (20,'20'),(100,'100'),
        )
    number_of_dice = models.IntegerField(default=1)
    number_of_dice.max_value = 100
    dice_walls = models.IntegerField(choices=POSSIBLE_DICE_WALL_NUMBERS, default=6)
    def __str__(self):
        return "number of dice:{}, dice walls:{}".format(self.number_of_dice, self.dice_walls)
    
class Results(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    result = models.IntegerField()
#    rolled_numbers = []
    def __str__(self):
        return str(self.result)
    
class RolledNumber(models.Model):
    value = models.IntegerField()
    result = models.ForeignKey(Results, on_delete=models.CASCADE)

    
            