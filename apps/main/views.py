from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .services import user
from django.utils import timezone
import requests



def index(request):
  key = "index"
  timenow = timezone.now()
  return render(request, 'index.html')


def login(request):

  return render(request, 'login.html')

@csrf_exempt 
def loginuser(request):
  User = user()

  if request.method == "GET":
    token_id = request.GET['tokenid']
    response = {'exists' : User.exists(token_id)}

    print (response)
    return (JsonResponse(response))

  if request.method == "POST":
    messages.success(request,f"fetching your details")
    print ("creating User")
    print (request.POST.dict)
    userCreated = User.create(request.POST)
    return(request)



