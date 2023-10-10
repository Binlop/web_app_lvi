from django.shortcuts import render
from .utils.processing_dna import ProcessingDna
from .forms import DNAAnalysisForm


def processing_dna(request):
    return render(request, "Processing_DNA/index.html")


def dna_analysis(request):
    if request.method == "POST":
        form = DNAAnalysisForm(request.POST)
        if form.is_valid():
            dna_sequence = form.cleaned_data["dna_sequence"]
            selected_properties = form.cleaned_data["properties"]
            processing_dna = ProcessingDna(
                dna_sequence, selected_properties
            )  # Создаем объект класса
            result = processing_dna.performing_functions()
            return render(
                request,
                "Processing_DNA/dna_analysis.html",
                {"form": form, "result": result},
            )
    else:
        form = DNAAnalysisForm()

    return render(request, "Processing_DNA/dna_analysis.html", {"form": form})
