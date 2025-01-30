from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'task_type', 'frequency', 
                  'duration', 'priority', 'physical_effort', 
                  'tiredness_factor']
        labels = {
            'duration': 'Duration(in minutes)',
        }