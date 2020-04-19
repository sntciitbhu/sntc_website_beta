from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

from .models import details,about_images,events,workshops,highlights

class FilterDetails(admin.ModelAdmin): 
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:  
            obj.user = request.user
            print("saved")
        obj.save()

    def get_queryset(self, request):
        if request.user.is_superuser:
            return details.objects.all()
        else:
            return details.objects.filter(user=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True 
        return obj.user == request.user or request.user.is_superuser

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('user') #here!
        return super(FilterDetails, self).get_form(request, obj, **kwargs)
    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

    fieldsets = [
        ("About The Club", {'fields': ["name","about","tagline","quote","logo_img"]}),
        ("External Links", {"fields": ["facebook","twitter","insta","git","youtube","linkedin"]}),
        ("Contact Us", {"fields": ["club_room_location","contact","email"]}) ,       
        ("Club Head", {"fields": ["user"]})        
    ]


class FilterImages(admin.ModelAdmin): 
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:  
            obj.user = request.user
            print("saved")
        obj.save()

    def get_queryset(self, request):
        if request.user.is_superuser:
            return about_images.objects.all()
        else:
            return about_images.objects.filter(user=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True 
        return obj.user == request.user or request.user.is_superuser

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('user') #here!
        return super(FilterImages, self).get_form(request, obj, **kwargs)


class FilterEvents(admin.ModelAdmin): 
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:  
            obj.user = request.user
            print("saved")
        obj.save()

    def get_queryset(self, request):
        if request.user.is_superuser:
            return events.objects.all()
        else:
            return events.objects.filter(user=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True 
        return obj.user == request.user or request.user.is_superuser

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('user') #here!
        return super(FilterEvents, self).get_form(request, obj, **kwargs)


class FilterWorkshops(admin.ModelAdmin): 
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:  
            obj.user = request.user
            print("saved")
        obj.save()

    def get_queryset(self, request):
        if request.user.is_superuser:
            return workshops.objects.all()
        else:
            return workshops.objects.filter(user=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True 
        return obj.user == request.user or request.user.is_superuser

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('user') #here!
        return super(FilterWorkshops, self).get_form(request, obj, **kwargs)



class FilterHighlights(admin.ModelAdmin): 
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:  
            obj.user = request.user
            print("saved")
        obj.save()

    def get_queryset(self, request):
        if request.user.is_superuser:
            return highlights.objects.all()
        else:
            return highlights.objects.filter(user=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True 
        return obj.user == request.user or request.user.is_superuser

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('user') #here!
        return super(FilterHighlights, self).get_form(request, obj, **kwargs)


admin.site.register(details,FilterDetails)
admin.site.register(about_images,FilterImages)
admin.site.register(events,FilterEvents)
admin.site.register(workshops,FilterWorkshops)
admin.site.register(highlights,FilterImages)
