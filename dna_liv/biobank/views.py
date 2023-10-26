from django.shortcuts import render, redirect
from .models import Biospecimen
from .forms import BiospecimenForm


# Create your views here.
def biobank_home(request):
    data = {
        'title': 'Биобанк',
    }
    return render(request, 'biobank/index.html', data)


def biospecimen(request):
    
    biospecimens = Biospecimen.objects.filter()[:10]
    return render(request, 'biobank/biospecimen.html', {'biospecimens': biospecimens})


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