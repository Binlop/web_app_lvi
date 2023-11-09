from django.shortcuts import render, redirect
from .models import Laboratory
from .forms import LabForm


# Create your views here.
def list_laboratories(request):
    labs = Laboratory.objects.filter()[:10]
    return render(request, 'biobank/laboratory/laboratories.html', {'labs': labs})


def create_lab(request):
    error = ''
    if request.method == 'POST':
        form = LabForm(request.POST, request.FILES)
        print(form.errors.items())
        if form.is_valid():
            lab = form.save(commit=False)  # Создаем объект, но не сохраняем его в базе данных пока
            lab.save()
            return redirect('list_laboratories')
        else:
            error = 'Форма была неверной'
    form = LabForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'biobank/laboratory/create_laboratory.html', data)