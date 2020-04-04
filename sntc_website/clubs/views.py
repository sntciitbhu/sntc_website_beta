from django.shortcuts import render
from django.http import HttpResponse
from .models import aero_head, aero_about_image, aero_highlight,aero_workshop,aero_event,aero_calendar,astro_head,astro_highlight,astro_workshop,astro_event,astro_calendar,biz_head,biz_highlight,biz_workshop,biz_event,biz_calendar,cops_head,cops_highlight,cops_workshop,cops_event,cops_calendar,csi_head,csi_highlight,csi_workshop,csi_event,csi_calendar,robo_head,robo_highlight,robo_workshop,robo_event,robo_calendar,sae_head,sae_highlight,sae_workshop,sae_event,sae_calendar

from django.utils import timezone

# Create your views here.
def aero(request):
  key = "aero"
  timenow = timezone.now()
  return render(request, 'clubs/club_page.html', {'about':aero_head.objects.all(),'about_images':aero_about_image.objects.all(),'highlight':aero_highlight,'workshops':aero_workshop.objects.order_by('-date'),'events':aero_event.objects.order_by('-date'),'calendar':aero_calendar, 'timenow':timenow,'key':key})
