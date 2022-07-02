from django.shortcuts import render


def index(request):
    return render(request, 'barber_panel.html')
