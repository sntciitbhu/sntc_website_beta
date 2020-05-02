from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .services import user
from django.utils import timezone
import requests

from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary[key]


User = user()

def index(request):
  key = "index"
  timenow = timezone.now()
  return render(request, 'index.html')

def dashboard(request):
  
  if "loggedin" not in request.session:
    return redirect('/login')

  else:
    print ("python is bewkoof")
    details = request.session['details']
    print (details)
    messages.success(request,"Signed in as "+request.session['name'])
    return render(request, 'dashboard.html', {'user': details})

def login(request):
  if "loggedin" in request.session:
    return redirect('/dashboard')

  else:
    return render(request, 'login.html')


@csrf_exempt 
def loginuser(request):

  if request.method == "GET":
    action = request.GET["action"]

    if action == "login":
      token_id = request.GET['tokenid']
      userDetails = User.getdetails(token_id)
      response = {'exists' : userDetails['exists']}
      if userDetails['exists']:
        request.session["name"] = userDetails['name']
        request.session["details"] = userDetails
        request.session["loggedin"] = True
        print(request.session["name"])

    elif action == "logout":
      del request.session["loggedin"]
      del request.session["name"]
      try:
        print(request.session["name"])
      except:
        print("no user found")

      response = {'logout' : True}

    return (JsonResponse(response))

  if request.method == "POST":
    print ("creating User")
    print (request.POST.dict)
    userDetails = User.create(request.POST)
    request.session["name"] = userDetails['name']
    request.session["loggedin"] = True
    return redirect('/dashboard')
