from django.shortcuts import render

from django.http import HttpResponse

from django.utils import timezone

from .models import tac_detail,tac_image,inventory_category,inventory,project_category,project,team,project_student,team_student


# Create your views here.

def tac(request):
  timenow = timezone.now()
  return render(request, 'tac.html', {'tac':tac_detail.objects.all()[0],'about_images':tac_image.objects.all(),'inventory_category':inventory_category.objects.all(),'project_categories':project_category.objects.all(),'project_list':project.objects.all(),'project_students':project_student.objects.all(),'inventory':inventory.objects.all(),'team_list':team.objects.all(),'team_students':team_student.objects.all()})		 
									 
									 
								