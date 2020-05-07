from apps.main.admin import admin
from django.db import models
import nested_admin


from .models import InputField,UploadField,SelectionField,Option,Form

class InputFieldDisplay(nested_admin.NestedTabularInline):
    model = InputField
    extra=0

class UploadFieldDisplay(nested_admin.NestedTabularInline):
    model = UploadField
    extra=0

class OptionsDisplay(nested_admin.NestedTabularInline):
    model = Option
    extra = 1

class SelectionFieldDisplay(nested_admin.NestedTabularInline):
    model = SelectionField
    extra=0
    inlines = [
        OptionsDisplay
    ]

class HiddenModels(nested_admin.NestedModelAdmin):

    def has_module_permission(self, request):
        return False

class FormDisplay(nested_admin.NestedModelAdmin):
    def has_module_permission(self, request):
        return False
    inlines = [
        InputFieldDisplay,
        UploadFieldDisplay,
        SelectionFieldDisplay,
    ]

admin.site.register(InputField, HiddenModels)
admin.site.register(UploadField, HiddenModels)
admin.site.register(SelectionField,HiddenModels)
admin.site.register(Option,HiddenModels)
admin.site.register(Form,FormDisplay)

