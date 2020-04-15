from django.shortcuts import render

from django.http import HttpResponse

from django.utils import timezone

from .models import  tac_detail,tac_image,inventory_category,inventory,project_categories,project_list,teams_list,project_students,team_students


# Create your views here.

def tac(request):
  timenow = timezone.now()
  return render(request, 'tac.html', {'tac':tac_detail.objects.all()[0],'about_images':tac_image.objects.all(),'inventory_category':inventory_category.objects.all(),'project_categories':project_categories.objects.all(),'project_list':project_list.objects.all(),'project_students':project_students.objects.all(),'inventory':inventory.objects.all(),'teams_list':teams_list.objects.all(),'team_students':team_students.objects.all()})		 
									 
									 
								