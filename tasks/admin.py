from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'task_type', 'user', 'priority', 'frequency')
    list_filter = ('task_type', 'user', 'priority', 'frequency')

admin.site.register(Task, TaskAdmin)
