from django import forms
from .models import Schedule, WorkoutTip, Workout

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['workout', 'date', 'time']

class WorkoutTipForm(forms.ModelForm):
    class Meta:
        model = WorkoutTip
        fields = ['workout_name', 'tip']
        
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Workout Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 3}),
        }