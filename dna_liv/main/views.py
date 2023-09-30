from django.shortcuts import render


def index(request):
    # Создание тестового словаря для вывода его значений на главную страницу сайта
    data = {'title': 'Главная страница',
            'values': ['some', 'Hello', '12323'],
            'obj': {
                'car': 'BMW',
                'age': '12',
                'country': 'ru'
            }
            }

    return render(request, 'main/index.html', data) # Добавлям объект, который отправляем


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')