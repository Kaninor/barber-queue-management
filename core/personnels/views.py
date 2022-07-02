from django.shortcuts import render


def index(request):
    return render(request, 'personnel_panel.html')
