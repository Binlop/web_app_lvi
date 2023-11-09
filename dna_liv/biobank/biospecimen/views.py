from django.shortcuts import render, redirect
from .models import Biospecimen
from biobank.storage.models import SampleLocation
from .forms import BiospecimenForm
from django.views.generic import UpdateView, DeleteView


class SampleUpdate(UpdateView):
    model = Biospecimen
    template_name = 'biobank/biospecimen/create_biospecimen.html'
    form_class = BiospecimenForm
    
    def get_object(self, queryset=None):
        biospecimen_id = self.kwargs['biospecimen_id']
        return Biospecimen.objects.get(pk=biospecimen_id)
    

def list_biospecimens(request):
    
    biospecimens = Biospecimen.objects.filter()[:10]
    return render(request, 'biobank/biospecimen/biospecimens.html', {'biospecimens': biospecimens})


def single_biospecimen(request, biospecimen_id):
    
    biospecimen = Biospecimen.objects.filter(id=biospecimen_id)[0]
    print('Это образец', biospecimen)
    return render(request, 'biobank/biospecimen/biospecimen.html', {'biospecimen': biospecimen})


def create_biospecimen(request):
    error = ''
    if request.method == 'POST':
        form = BiospecimenForm(request.POST, request.FILES)
        print(form.errors.items())
        if form.is_valid():
            biospecimen = form.save(commit=False)  # Создаем объект, но не сохраняем его в базе данных пока
            biospecimen.file_name = str(request.FILES.get('file'))  # Получаем название файла
            project_instance = form.cleaned_data['project']
            print(project_instance)
            biospecimen.project = project_instance
            sample_storage_id = biospecimen.location_id
            location = SampleLocation.objects.get(id=sample_storage_id)
            biospecimen.name_storage_sample = location
            print(f'Это location {location}')
            location.state_location = 'Занято'  # Измените на нужное состояние
            biospecimen.save()  # Теперь сохраняем объект
            print('Это айди образца биологического', biospecimen.id)
            location.sample_id = biospecimen.id
            location.save()
            return redirect('list_biospecimens')
        else:
            error = 'Форма была неверной'
    form = BiospecimenForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'biobank/biospecimen/create_biospecimen.html', data)