from .models import Biospecimen, Freezer, Shelf, Box, SampleLocation
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, ClearableFileInput, ModelMultipleChoiceField, ModelChoiceField, SelectMultiple, Select  #Импорт необходимых виджетов
from django import forms

# Создаем отдельный класс, который будет именно отображать модель Biospecimen на сайте
class BiospecimenForm(ModelForm):
    location = ModelChoiceField(
        queryset=SampleLocation.objects.filter(state_location='free'),
        widget=Select(attrs={
            'class': 'form-control',
            'placeholder': "Место хранения образца",
        }))
    class Meta:
        model = Biospecimen #Наследуем модель из БД
        
        fields = ['title', 'test_field', 'location', 'date', 'file'] #Задаем необходимые поля на сайте, имена поля на сайте и в БД могут отличатья

        # Создаем словарь виджетов(полей), как они будут отображаться на странице
        widgets = {
            'title': TextInput(attrs={ #Указываем сам виджет, который будем использовать
                'class': 'form-control', #Указываем стиль отображения из boostrap
                'placeholder': "Название образца", #Указываем название этого поля на странице
            }),
            'test_field': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Тестовое поле",

            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': "Дата получения"
            }),
            'file': ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': "Ваш файл"
            }),
        }
    def __init__(self, *args, **kwargs):
        super(BiospecimenForm, self).__init__(*args, **kwargs)
        self.fields['test_field'].required = False
class FreezerForm(ModelForm):
    class Meta:
        model = Freezer
        fields = ['title']
        widgets = {
            'title': TextInput(attrs={ #Указываем сам виджет, который будем использовать
                'class': 'form-control', #Указываем стиль отображения из boostrap
                'placeholder': "Название морозилки", #Указываем название этого поля на странице

            }),
        }

class ShelfForm(ModelForm):
    class Meta:
        model = Shelf
        fields = ['title']
        widgets = {
            'title': TextInput(attrs={ #Указываем сам виджет, который будем использовать
                'class': 'form-control', #Указываем стиль отображения из boostrap
                'placeholder': "Название полки", #Указываем название этого поля на странице

            }),
        }

class BoxForm(ModelForm):
    class Meta:
        model = Box
        fields = ['title']
        widgets = {
            'title': TextInput(attrs={ #Указываем сам виджет, который будем использовать
                'class': 'form-control', #Указываем стиль отображения из boostrap
                'placeholder': "Название коробки", #Указываем название этого поля на странице

            }),
        }
        
class SampleForm(ModelForm):
    class Meta:
        model = SampleLocation
        fields = ['title', 'count_samples', 'count_rows', 'count_col']
        widgets = {
            'title': TextInput(attrs={ #Указываем сам виджет, который будем использовать
                'class': 'form-control', #Указываем стиль отображения из boostrap
                'placeholder': "Название образцов", #Указываем название этого поля на странице

            }),
            'count_samples': TextInput(attrs={ #Указываем сам виджет, который будем использовать
                'class': 'form-control', #Указываем стиль отображения из boostrap
                'placeholder': "Название коробки", #Указываем название этого поля на странице

            }),
            'count_rows': TextInput(attrs={ #Указываем сам виджет, который будем использовать
                'class': 'form-control', #Указываем стиль отображения из boostrap
                'placeholder': "Название коробки", #Указываем название этого поля на странице

            }),
            'count_col': TextInput(attrs={ #Указываем сам виджет, который будем использовать
                'class': 'form-control', #Указываем стиль отображения из boostrap
                'placeholder': "Название коробки", #Указываем название этого поля на странице

            }),
        }