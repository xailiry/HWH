from django import forms

from .models import HomeTask


class HometaskForm(forms.ModelForm):
    class Meta:
        model = HomeTask
        fields = ['subject', 'task_text', 'due_date', 'status']  # Поля, которые будут в форме
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-control'}),  # Виджет для выпадающего списка предметов
            'task_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),  # Виджет для текста задания
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),  # Виджет для даты
            'status': forms.Select(attrs={'class': 'form-control'}),  # Выпадающий список для статуса
        }
        labels = {
            'subject': 'Предмет',
            'task_text': 'Текст задания',
            'due_date': 'Срок выполнения',
            'status': 'Статус',
        }
