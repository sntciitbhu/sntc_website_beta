from django.shortcuts import render
from django.http import HttpResponse

def technex(request):
    sections = [
        'PR - (Talks and exhibitions)',
        "Events",
        'workshops',
        "chota sa kelaidoscope"
    ]
    return render(request, 'technex.html')
    return HttpResponse('hello')