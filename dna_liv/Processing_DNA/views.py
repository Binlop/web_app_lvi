from django.shortcuts import render, redirect
from .forms import DNASequenceForm
from .utils.processing_dna import ProcessingDna
from .forms import DNAAnalysisForm

def processing_dna(request):
    return render(request, 'Processing_DNA/index.html')

def dna_length_add(request):
    if request.method == 'POST':
        form = DNASequenceForm(request.POST)
        if form.is_valid():
            dna_sequence = form.cleaned_data['sequence']
            len_seq = ProcessingDna.count_len_dna(dna_sequence)
            return render(request, 'Processing_DNA/add_length.html', {'form': form, 'processed_data': len_seq})
    else:
        form = DNASequenceForm()  # Создаем пустую форму, если это GET запрос
        return render(request, 'Processing_DNA/add_length.html', {'form': form})
    # return render(request, 'Processing_DNA/add_length.html', {'form': form})

def dna_analysis(request):
    if request.method == 'POST':
        form = DNAAnalysisForm(request.POST)
        if form.is_valid():
            dna_sequence = form.cleaned_data['dna_sequence']
            selected_properties = form.cleaned_data['properties']
            processing_dna = ProcessingDna(dna_sequence, selected_properties)
            result = processing_dna.performing_functions()
            return render(request, 'Processing_DNA/dna_analysis.html', {'form': form, 'result': result})
    else:
        form = DNAAnalysisForm()

    return render(request, 'Processing_DNA/dna_analysis.html', {'form': form})





