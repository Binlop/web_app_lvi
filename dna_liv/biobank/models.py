from django.db import models

# Create your models here.
class Biospecimen(models.Model): #Обязательное наследование разных типов полей
    # Указываем виджет поля, его название, кол-во символов в поле, значенеи по умолчанию
    title = models.CharField('Название образца', max_length=50, default='')
    test_field = models.CharField('Тестовое поле', max_length=250, default='')
    date = models.DateTimeField('Дата получения')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/biobank/{self.id}'

    # Для нормального отображения в панели администратора таблицы Новость в ед и мн.ч
    class Meta:
        verbose_name = 'Биологический образец'
        verbose_name_plural = 'Биологические образцы'