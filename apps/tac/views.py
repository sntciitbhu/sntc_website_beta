from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

from django.utils import timezone

from .models import bigbook,facilities, guidelines,inventory_category,project_list,projects,tac_head,tac_image,teams_list,techteams,team_students,students,categories

# Create your views here.

def tac(request):
  timenow = timezone.now()
  return render(request, 'tac.html', {'about':tac_head.objects.all(),'about_images':tac_image.objects.all()})