from django.forms import ModelForm
from .models import Task
from django.forms import ModelForm

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
