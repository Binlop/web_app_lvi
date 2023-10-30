from .models import Biospecimen
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, ClearableFileInput #Импорт необходимых виджетов

# Создаем отдельный класс, который будет именно отображать модель Biospecimen на сайте
class BiospecimenForm(ModelForm):
    class Meta:
        model = Biospecimen #Наследуем модель из БД
        fields = ['title', 'test_field', 'date', 'file'] #Задаем необходимые поля на сайте, имена поля на сайте и в БД могут отличатья

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