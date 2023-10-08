from django import forms
from .models import Task, TaskPhoto


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'complete']
        widgets = {
            'due_date': forms.TextInput(attrs={'type': 'datetime-local'}),
        }
class TaskPhotoForm(forms.ModelForm):
    class Meta:
        model = TaskPhoto
        fields = ['photo']