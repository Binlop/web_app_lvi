from django.db import models

class Freezer(models.Model):
    title = models.CharField(max_length=100)
    # Другие поля морозилки

    def __str__(self):
        return self.title


class Shelf(models.Model):
    title = models.CharField(max_length=100)
    freezer = models.ForeignKey(Freezer, on_delete=models.CASCADE)
    # Другие поля полки

    def __str__(self):
        return self.title


class Box(models.Model):
    title = models.CharField(max_length=100)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    # Другие поля коробки

    def __str__(self):
        return self.title
    

class SampleLocation(models.Model):
    title = models.CharField(max_length=100)
    count_samples = models.IntegerField(default=0)
    count_rows = models.IntegerField(default=0)
    count_col = models.IntegerField(default=0)
    state_location = models.CharField(max_length=10, default='free')
    sample_id = models.IntegerField(default=-1)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    # Другие поля места

    def __str__(self):
        return self.title


class Biospecimen(models.Model): #Обязательное наследование разных типов полей
    """Модель характеризует биологический образец, его поля и необходима для его регистрации в БД. Поля в дальнейшем будут расширяться"""
    # Указываем виджет поля, его название, кол-во символов в поле, значение по умолчанию
    title = models.CharField('Название образца', max_length=50, default='')
    test_field = models.CharField('Тестовое поле', max_length=250, default='')
    date = models.DateTimeField('Дата получения')
    file_name = models.CharField('Название файла', max_length=50)
    file = models.FileField(upload_to = 'upldfile/')
    name_storage_sample = models.CharField('Место хранения образца в хранилище', max_length=100, default='')
    location = models.ForeignKey(SampleLocation, on_delete=models.CASCADE, default='')

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
