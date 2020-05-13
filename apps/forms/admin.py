from apps.main.admin import admin
from django.db import models
import nested_admin


from .models import Field,Option,Form


class OptionsDisplay(nested_admin.NestedTabularInline):
    model = Option
    extra = 1


class FieldDisplay(nested_admin.NestedTabularInline):
    model = Field
    extra = 0
    
    inlines = [
        OptionsDisplay
    ]

class HiddenModels(nested_admin.NestedModelAdmin):

    def has_module_permission(self, request):
        return False



    


class FormDisplay(nested_admin.NestedModelAdmin):
    def has_module_permission(self, request):
        return False

    change_form_template = 'forms_change_form.html'

        
    inlines = [
        FieldDisplay
    ]

admin.site.register(Field,HiddenModels)
admin.site.register(Option,HiddenModels)
admin.site.register(Form,FormDisplay)

