from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


# Create your views here.
def news_home(request):
    news = Articles.objects.order_by('-date')[:5] #Создаем объект новостей из базы данных и сортировка записей по дате(самые новые сверху)
    return render(request, 'news/index.html', {'news':news}) #Отправляем объекты новостей на сайт


def news_create(request):
    error = ''
    if request.method == 'POST': #Проверяем, что данные из формы были отправлены с помощью метода POST
        form = ArticlesForm(request.POST) #Создаем переменную на основе объекта из формы
        if form.is_valid(): #Проверяем соответствие полей типам данных и сохраняем форму в БД
            form.save()
            return redirect('home') #После сохранения переносим пользователя на домашнюю страницу
        else:
            error = 'Форма была неверной'

    form = ArticlesForm #Создаем форму на основе модели(таблицы) в БД

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)  #Отправка формы или ошибки на страницу содания новости