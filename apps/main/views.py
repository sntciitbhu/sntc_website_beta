from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .services import user
from django.utils import timezone
import logging
import requests
from django import template


from django.template.defaulttags import register

logger = logging.getLogger(__name__)

register = template.Library()

@register.filter
def get_item(dictionary, key):
  return dictionary[key]

@register.filter
def split(str, key):
  str = str.split(key)[0]
  return str



User = user()

def index(request):
  key = "index"
  timenow = timezone.now()
  return render(request, 'index.html')

def dashboard(request):
  
  if "loggedin" not in request.session:
    return redirect('/login')

  else:
    details = request.session['details']
    logger.info (details)
    print(details)
    print(request.session['name'])
    details['bday'] = details['bday'].split("T")[0]
    return render(request, 'dashboard.html', {'user': details})
    

def login(request):
  if "loggedin" in request.session:
    messages.success(request,"Signed in as "+request.session['name'])
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
        logger.info(request.session["name"])

    elif action == "logout":
      del request.session["loggedin"]
      del request.session["name"]
      del request.session["details"]
      try:
        logger.info(request.session["name"])
      except:
        logger.info("no user found")

      response = {'logout' : True}

    return (JsonResponse(response))

  if request.method == "POST":
    logger.info ("creating User")
    logger.info (request.POST.dict)
    userDetails = User.create(request.POST)
    request.session["name"] = userDetails['name']
    request.session["details"] = userDetails
    request.session["loggedin"] = True
    return redirect('/dashboard')

@csrf_exempt 
def dashaction(request):
  if request.method == "POST":
    logger.info ("Updating User")
    logger.info (request.POST.dict)
    action = request.POST.get("action")
    print(action)
    userDetails = User.update(request.POST, action)
    request.session["name"] = userDetails['name']
    request.session["details"] = userDetails
    request.session["loggedin"] = True
    messages.success(request,"Profile Update")
    response = {'update': True}
    return redirect('/dashboard')


