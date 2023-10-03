from django.shortcuts import render, redirect
from .forms import DNASequenceForm
from .utils.processing_dna import ProcessingDna

def processing_dna(request):
    return render(request, 'Processing_DNA/index.html')

def dna_length_add(request):
    if request.method == 'POST':
        form = DNASequenceForm(request.POST)
        if form.is_valid():
            dna_sequence = form.cleaned_data['sequence']
            len_seq = ProcessingDna.count_len_dna(dna_sequence)
            # Делайте что-то с данными из формы, например, сохраняйте их в базу данных
            # Затем перенаправьте пользователя на другую страницу или отобразите сообщение об успехе
            return render(request, 'Processing_DNA/add_length.html', {'form': form, 'processed_data': len_seq})
    else:
        form = DNASequenceForm()  # Создаем пустую форму, если это GET запрос
        return render(request, 'Processing_DNA/add_length.html', {'form': form})
    # return render(request, 'Processing_DNA/add_length.html', {'form': form})
