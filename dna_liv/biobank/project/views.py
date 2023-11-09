from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


# Create your views here.
def list_projects(request):
    
    projects = Project.objects.filter()[:10]
    return render(request, 'biobank/project/projects.html', {'projects': projects})


def create_project(request):
    error = ''
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        error = form.errors.items()
        if form.is_valid():
            project = form.save(commit=False)  # Создаем объект, но не сохраняем его в базе данных пока
            laboratory_instance = form.cleaned_data['laboratory']
            project.laboratory = laboratory_instance
            project.save()
            return redirect('list_projects')
        else:
            error = 'Форма была неверной'
    
    form = ProjectForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'biobank/project/create_project.html', data)