import shortuuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.CharField(
        primary_key=True,
        default=shortuuid.uuid,
        max_length=22,
        editable=False
    )
    name = models.CharField(max_length=100)
    task_type = models.CharField(max_length=50, choices=[
        ('work', 'Work'),
        ('exercise', 'Exercise'),
        ('household', 'Household'),
        ('leisure', 'Leisure'),
    ])
    frequency = models.CharField(max_length=50, choices=[  
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ])
    duration = models.SmallIntegerField(validators=[MinValueValidator(1)]) 
    priority = models.CharField(max_length=50, choices=[ 
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ])
    physical_effort = models.CharField(max_length=50, choices=[  
        ('light', 'Light'),
        ('moderate', 'Moderate'),
        ('intense', 'Intense'),
    ])
    tiredness_factor = models.CharField(max_length=50, choices=[
        ('relaxing', 'Relaxing'),
        ('neutral', 'Neutral'),
        ('draining', 'Draining')
    ]) 
    
    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name