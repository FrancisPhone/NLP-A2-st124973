from django.shortcuts import render
from .utils import generate


def index(request):
    results = list()
    prompt = request.GET.get("prompt", "")
    temperatures = [0.5, 0.7, 0.75, 0.8, 1.0]
    if prompt:
        for temperature in temperatures:
            results.append(generate(prompt=prompt, temperature=temperature))

    return render(request, 'index.html',
                  {'generated_results': zip(temperatures, results)})
