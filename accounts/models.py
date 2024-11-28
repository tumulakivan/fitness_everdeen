from django.db import models
from django.contrib.auth.models import User

class Schedule(models.Model):
    workout = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.workout} on {self.date} at {self.time}"

class WorkoutTip(models.Model):
    workout_name = models.CharField(max_length=100)
    tip = models.TextField()

    def __str__(self):
        return self.workout_name
    
class Workout(models.Model):
    WORKOUT_TYPE_CHOICES = [
        ('strength', 'Strength'),
        ('cardio', 'Cardio'),
        ('flexibility', 'Flexibility'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    workout_type = models.CharField(max_length=50, choices=WORKOUT_TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name