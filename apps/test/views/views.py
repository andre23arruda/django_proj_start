from django.shortcuts import render

def blank(request):
    context = { 'page_title': 'Página em branco' }
    return render(request, 'test/index.html', context)