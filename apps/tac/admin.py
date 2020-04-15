from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models


class head_text(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

       
from .models import tac_detail,tac_image,inventory_category,inventory,project_categories,project_list,teams_list,project_students,team_students
 
admin.site.register(tac_detail,head_text)
admin.site.register(tac_image,head_text)
admin.site.register(inventory_category,head_text)
admin.site.register(inventory,head_text)
admin.site.register(project_categories,head_text)
admin.site.register(project_list,head_text)
admin.site.register(teams_list,head_text)
admin.site.register(project_students,head_text)
admin.site.register(team_students,head_text)