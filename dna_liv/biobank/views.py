from django.shortcuts import render, redirect
from .models import Biospecimen
from .forms import BiospecimenForm
""""Представление различных разделов биобанка прописано здесь"""


# Отображение главной страницы
def biobank_home(request):
    data = {
        'title': 'Биобанк',
    }
    return render(request, 'biobank/index.html', data)


# Отображение раздела биологические образцы
def biospecimen(request):
    
    biospecimens = Biospecimen.objects.filter()[:10]
    return render(request, 'biobank/biospecimen.html', {'biospecimens': biospecimens})


# Отображение формы для добавления биологического образца
def create_biospecimen(request):
    error = ''
    if request.method == 'POST':
        form = BiospecimenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('biospecimen')
        else:
            error = 'Форма была неверной'
    form = BiospecimenForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'biobank/create_object.html', data)