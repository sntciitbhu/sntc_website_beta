from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

from django.utils import timezone

# Create your views here.

def index(request):
  key = "index"
  timenow = timezone.now()
  return render(request, 'index.html')

def login(request):
  key = "index"
  return render(request, 'login.html')
