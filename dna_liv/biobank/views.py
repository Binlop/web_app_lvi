from django.shortcuts import render, redirect
from .models import Biospecimen, Freezer, Shelf, Box, SampleLocation
from .forms import BiospecimenForm, FreezerForm, ShelfForm, BoxForm, SampleForm, ModelForm
from django.views.generic import UpdateView, DeleteView #Динамически изменяемый url адрес
""""Представление различных разделов биобанка прописано здесь"""


# Отображение главной страницы
def biobank_home(request):
    data = {
        'title': 'Биобанк',
    }
    return render(request, 'biobank/index.html', data)

class SampleUpdate(UpdateView):
    model = Biospecimen
    template_name = 'biobank/biospecimen/create_biospecimen.html'
    form_class = BiospecimenForm
    
    def get_object(self, queryset=None):
        biospecimen_id = self.kwargs['biospecimen_id']
        return Biospecimen.objects.get(pk=biospecimen_id)

# Отображение раздела биологические образцы
def list_biospecimens(request):
    
    biospecimens = Biospecimen.objects.filter()[:10]
    return render(request, 'biobank/biospecimen/biospecimens.html', {'biospecimens': biospecimens})

def single_biospecimen(request, biospecimen_id):
    
    biospecimen = Biospecimen.objects.filter(id=biospecimen_id)[0]
    print('Это образец', biospecimen)
    return render(request, 'biobank/biospecimen/biospecimen.html', {'biospecimen': biospecimen})


# Отображение формы для добавления биологического образца
def create_biospecimen(request):
    error = ''
    if request.method == 'POST':
        form = BiospecimenForm(request.POST, request.FILES)
        print(form.errors.items())
        if form.is_valid():
            biospecimen = form.save(commit=False)  # Создаем объект, но не сохраняем его в базе данных пока
            biospecimen.file_name = str(request.FILES.get('file'))  # Получаем название файла
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


def storage_view(request):
    freezers = Freezer.objects.filter()[:10]
    return render(request, 'biobank/storage/storage.html', {'freezers': freezers})


def create_freezer(request):
    error = ''
    if request.method == 'POST':
        form = FreezerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('storage_view')
        else:
            error = 'Форма была неверной'
    form = FreezerForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'biobank/biospecimen/create_biospecimen.html', data)


def freezer_view(request, freezer_id):
    shelfs = Shelf.objects.filter(freezer_id=freezer_id)[:10]
    return render(request, 'biobank/storage/freezer.html', {'shelfs': shelfs, 'freezer_id': freezer_id})


def create_shelf(request, freezer_id):
    error = ''
    if request.method == 'POST':
        form = ShelfForm(request.POST)
        if form.is_valid():
            shelf = form.save(commit=False)  # Создаем объект, но не сохраняем его в базе данных пока
            shelf.freezer_id = freezer_id  # Получаем название файла
            shelf.save()  # Теперь сохраняем объект
            return redirect('freezer_view', freezer_id=freezer_id)
        else:
            error = 'Форма была неверной'
    form = ShelfForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'biobank/biospecimen/create_biospecimen.html', data)


def shelf_view(request, shelf_id, freezer_id):
    boxes = Box.objects.filter(shelf_id=shelf_id)[:10]
    return render(request, 'biobank/storage/shelf.html', {'boxes': boxes, 'shelf_id': shelf_id, 'freezer_id': freezer_id})


def create_box(request, freezer_id, shelf_id):
    error = ''
    if request.method == 'POST':
        form = BoxForm(request.POST)
        if form.is_valid():
            shelf = form.save(commit=False)  # Создаем объект, но не сохраняем его в базе данных пока
            shelf.shelf_id = shelf_id  # Получаем название файла
            shelf.save()  # Теперь сохраняем объект
            return redirect('shelf_view', freezer_id, shelf_id)
        else:
            error = 'Форма была неверной'
    form = BoxForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'biobank/biospecimen/create_biospecimen.html', data)


def box_view(request, freezer_id, shelf_id, box_id):
    samples = SampleLocation.objects.filter(box_id=box_id)
    samples_occupied = SampleLocation.objects.filter(box_id=box_id, state_location='Занято')
    if samples.exists():
        count_rows = samples.first().count_rows
        # count_rows = 10
        count_col = samples.first().count_col
        all_samples = len(samples)
        samples_occupied = len(samples_occupied)
        samples_free = all_samples - samples_occupied
        # count_col = 10
        samples_grid = []
        for i in range(count_rows):
            row = samples[i * count_col: (i + 1) * count_col]
            samples_grid.append(row)
    else:
        samples_grid = []
        samples_free = 0
        samples_occupied = 0
        count_rows = 0 
        count_col = 0
        all_samples = 0      
    return render(request, 'biobank/storage/box.html', {'samples_grid': samples_grid, 'freezer_id': freezer_id, 'shelf_id': shelf_id, 'box_id': box_id,
                                                        'num_rows': range(count_rows), 'num_cols': range(count_col), 'all_samples': all_samples,
                                                        'samples_occupied': samples_occupied, 'samples_free': samples_free, 'samples_id': range(all_samples)
                                                        })


def create_sample(request, freezer_id, shelf_id, box_id):
    error = ''
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            count_samples = form.cleaned_data.get('count_samples') or 0 # Получите количество образцов из формы
            count_rows = form.cleaned_data.get('count_rows') or 0  # Получите количество образцов из формы
            count_col = form.cleaned_data.get('count_col') or 0 # Получите количество образцов из формы
            title = form.cleaned_data.get('title')  # Получите количество образцов из формы
            for _ in range(count_samples):
                sample = SampleLocation(title=f'Морозильник{freezer_id}_Полка{shelf_id}_Коробка{box_id}_{title}{_}', count_samples=count_samples, box_id = box_id, count_rows=count_rows, count_col=count_col)
                sample.save()

            return redirect('box_view', freezer_id, shelf_id, box_id)
        else:
            error = 'Форма была неверной'
    form = SampleForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'biobank/biospecimen/create_biospecimen.html', data)
