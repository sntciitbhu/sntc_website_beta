from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models


class head_text(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

       
from .models import bigbook,facilities, guidelines,inventory_category,project_list,projects,tac_head,tac_image,teams_list,techteams,team_students,students,categories

admin.site.register(tac_head,head_text)
admin.site.register(tac_image,head_text)
admin.site.register(facilities,head_text)

admin.site.register(guidelines,head_text)

admin.site.register(projects,head_text)
admin.site.register(bigbook,head_text)

admin.site.register(project_list,head_text)
admin.site.register(techteams,head_text)

admin.site.register(teams_list,head_text)


admin.site.register(inventory_category,head_text)
admin.site.register(categories,head_text)
admin.site.register(students,head_text)
admin.site.register(team_students,head_text)
