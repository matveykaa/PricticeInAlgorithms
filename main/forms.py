from .models import Task1, Task2
from django.forms import ModelForm, TextInput, Textarea, IntegerField


class Task1Form(ModelForm):
    class Meta:
        model = Task1
        fields = ["words1", "words2"]
        widgets = {
            "words1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter words1"
            }),
            "words2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter words2"
            })
        }

class Task2Form(ModelForm):
    class Meta:
        model = Task2
        fields = ["massiv", "target"]
        widgets = {
            "massiv": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter array"
            }),
            "target": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter target"
            })
        }