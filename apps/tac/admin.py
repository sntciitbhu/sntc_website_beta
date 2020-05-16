from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

from .models import tac_detail,tac_image,inventory_category,inventory,project_category,project,team,project_student,team_student

class hiddenDisplay(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
    def has_module_permission(self, request):
        return False

class DisplayTACImage(admin.StackedInline):
    model = tac_image
    extra = 3

class DisplayProjectStudents(admin.TabularInline):
    model = project_student
    extra = 1

class DisplayTeamStudents(admin.TabularInline):
    model = team_student
    extra = 1


class DisplayProject(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
    inlines = [
        DisplayProjectStudents
    ]

class DisplayTeam(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

    inlines = [
        DisplayTeamStudents
    ]

class normalDisplay(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

class tac_detailDisplay(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }    
    
    fieldsets = [
        ("About TAC", {'fields': ["name","about_tac","tagline",("logo","logo_black")]}),
        ("External Links", {"fields": ["facebook","twitter","insta","git","youtube","linkedin"]}),
        ("Contact Us", {"fields": ["location","contact_number","email"]}) ,  
        ("Inventory", {"fields": ["about_facilites","guidelines","inventory_bg_image"]}) ,       
        ("Projects", {"fields": ["project_content","project_image"]}) ,       
        ("Big Book and Technical Teams", {"fields": ["bigbook_content","bigbook_bg_image","technical_teams_content"]}) ,
    ]
 
admin.site.register(tac_detail,tac_detailDisplay)
admin.site.register(tac_image,hiddenDisplay)

admin.site.register(inventory_category,hiddenDisplay)
admin.site.register(inventory,normalDisplay)

admin.site.register(project_category,hiddenDisplay)
admin.site.register(project,DisplayProject)
admin.site.register(project_student,hiddenDisplay)

admin.site.register(team,DisplayTeam)
admin.site.register(team_student,hiddenDisplay)