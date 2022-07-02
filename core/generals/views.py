from django.shortcuts import render

def panel(request):
    return render(request, "panels.html")
