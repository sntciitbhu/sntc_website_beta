from django.shortcuts import render
from django.http import HttpResponse

from django.utils import timezone

from django.urls import resolve

# Create your views here.

from .models import details,about_images,events,workshops,highlights


def aero(request):
  key = 'aero'
  timenow = timezone.now()
  return render(request, 'clubs/club_page.html', {'club':details.objects.filter(user__username=key).first(),'about_images':about_images.objects.filter(user__username=key),'highlights':highlights.objects.filter(user__username=key),'workshops':workshops.objects.filter(user__username=key).order_by('-date'),'events':events.objects.filter(user__username=key).order_by('-date'),'timenow':timenow,'key':key})

def astro(request):
  key = 'astro'
  timenow = timezone.now()
  return render(request, 'clubs/club_page.html', {'club':details.objects.filter(user__username=key).first(),'about_images':about_images.objects.filter(user__username=key),'highlights':highlights.objects.filter(user__username=key),'workshops':workshops.objects.filter(user__username=key).order_by('-date'),'events':events.objects.filter(user__username=key).order_by('-date'),'timenow':timenow,'key':key})

def biz(request):
  key = 'biz'
  timenow = timezone.now()
  return render(request, 'clubs/club_page.html', {'club':details.objects.filter(user__username=key).first(),'about_images':about_images.objects.filter(user__username=key),'highlights':highlights.objects.filter(user__username=key),'workshops':workshops.objects.filter(user__username=key).order_by('-date'),'events':events.objects.filter(user__username=key).order_by('-date'),'timenow':timenow,'key':key})

def csi(request):
  key = 'csi'
  timenow = timezone.now()
  return render(request, 'clubs/club_page.html', {'club':details.objects.filter(user__username=key).first(),'about_images':about_images.objects.filter(user__username=key),'highlights':highlights.objects.filter(user__username=key),'workshops':workshops.objects.filter(user__username=key).order_by('-date'),'events':events.objects.filter(user__username=key).order_by('-date'),'timenow':timenow,'key':key})

def cops(request):
  key = 'cops'
  timenow = timezone.now()
  return render(request, 'clubs/club_page.html', {'club':details.objects.filter(user__username=key).first(),'about_images':about_images.objects.filter(user__username=key),'highlights':highlights.objects.filter(user__username=key),'workshops':workshops.objects.filter(user__username=key).order_by('-date'),'events':events.objects.filter(user__username=key).order_by('-date'),'timenow':timenow,'key':key})

def robo(request):
  key = 'robo'
  timenow = timezone.now()
  return render(request, 'clubs/club_page.html', {'club':details.objects.filter(user__username=key).first(),'about_images':about_images.objects.filter(user__username=key),'highlights':highlights.objects.filter(user__username=key),'workshops':workshops.objects.filter(user__username=key).order_by('-date'),'events':events.objects.filter(user__username=key).order_by('-date'),'timenow':timenow,'key':key})

def sae(request):
  key = 'sae'
  timenow = timezone.now()
  return render(request, 'clubs/club_page.html', {'club':details.objects.filter(user__username=key).first(),'about_images':about_images.objects.filter(user__username=key),'highlights':highlights.objects.filter(user__username=key),'workshops':workshops.objects.filter(user__username=key).order_by('-date'),'events':events.objects.filter(user__username=key).order_by('-date'),'timenow':timenow,'key':key})


