from django.shortcuts import render
from django.http import HttpResponse

from django.utils import timezone

# Create your views here.

from .models import aero_head,aero_about_image, aero_highlight,aero_workshop,aero_event

def aero(request):
  key = "aero"
  timenow = timezone.now()
  return render(request, 'clubs/club_page.html', {'about':aero_head.objects.all(),'about_images':aero_about_image.objects.all(),'highlights':aero_highlight.objects.all(),'workshops':aero_workshop.objects.order_by('-date'),'events':aero_event.objects.order_by('-date'),'timenow':timenow,'key':key})


from .models import astro_head,astro_about_image, astro_highlight,astro_workshop,astro_event

def astro(request):
  key = "astro"
  timenow = timezone.now()
  return render(request, 'clubs/club_page.html', {'about':astro_head.objects.all(),'about_images':astro_about_image.objects.all(),'highlights':astro_highlight.objects.all(),'workshops':astro_workshop.objects.order_by('-date'),'events':astro_event.objects.order_by('-date'),'timenow':timenow,'key':key})


from .models import biz_head,biz_about_image, biz_highlight,biz_workshop,biz_event

def biz(request):
  key = "biz"
  timenow = timezone.now()
  return render(request, 'clubs/club_page.html', {'about':biz_head.objects.all(),'about_images':biz_about_image.objects.all(),'highlights':biz_highlight.objects.all(),'workshops':biz_workshop.objects.order_by('-date'),'events':biz_event.objects.order_by('-date'),'timenow':timenow,'key':key})

from .models import csi_head,csi_about_image, csi_highlight,csi_workshop,csi_event

def csi(request):
  key = "csi"
  timenow = timezone.now()
  return render(request, 'clubs/club_page.html', {'about':csi_head.objects.all(),'about_images':csi_about_image.objects.all(),'highlights':csi_highlight.objects.all(),'workshops':csi_workshop.objects.order_by('-date'),'events':csi_event.objects.order_by('-date'),'timenow':timenow,'key':key})


from .models import cops_head,cops_about_image, cops_highlight,cops_workshop,cops_event

def cops(request):
  key = "cops"
  timenow = timezone.now()
  return render(request, 'clubs/club_page.html', {'about':cops_head.objects.all(),'about_images':cops_about_image.objects.all(),'highlights':cops_highlight.objects.all(),'workshops':cops_workshop.objects.order_by('-date'),'events':cops_event.objects.order_by('-date'),'timenow':timenow,'key':key})

from .models import robo_head,robo_about_image, robo_highlight,robo_workshop,robo_event

def robo(request):
  key = "robo"
  timenow = timezone.now()
  return render(request, 'clubs/club_page.html', {'about':robo_head.objects.all(),'about_images':robo_about_image.objects.all(),'highlights':robo_highlight.objects.all(),'workshops':robo_workshop.objects.order_by('-date'),'events':robo_event.objects.order_by('-date'),'timenow':timenow,'key':key})

from .models import sae_head,sae_about_image, sae_highlight,sae_workshop,sae_event

def sae(request):
  key = "sae"
  timenow = timezone.now()
  return render(request, 'clubs/club_page.html', {'about':sae_head.objects.all(),'about_images':sae_about_image.objects.all(),'highlights':sae_highlight.objects.all(),'workshops':sae_workshop.objects.order_by('-date'),'events':sae_event.objects.order_by('-date'),'timenow':timenow,'key':key})


