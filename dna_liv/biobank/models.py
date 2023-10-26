from django.db import models

class Biospecimen(models.Model): #Обязательное наследование разных типов полей
    """Модель характеризует биологический образец, его поля и необходима для его регистрации в БД. Поля в дальнейшем будут расширяться"""
    # Указываем виджет поля, его название, кол-во символов в поле, значение по умолчанию
    title = models.CharField('Название образца', max_length=50, default='')
    test_field = models.CharField('Тестовое поле', max_length=250, default='')
    date = models.DateTimeField('Дата получения')

    # Для корректного отображения в админ-панели
    def __str__(self):
        return self.title

    # Неизвестно для чего
    def get_absolute_url(self):
        return f'/biobank/{self.id}'

    # Для нормального отображения в панели администратора таблицы Новость в ед и мн.ч
    class Meta:
        verbose_name = 'Биологический образец'
        verbose_name_plural = 'Биологические образцы'