from django.contrib import admin
from .models import aero_head,aero_about_image, aero_highlight,aero_workshop,aero_event,aero_calendar,astro_head,astro_highlight,astro_workshop,astro_event,astro_calendar,biz_head,biz_highlight,biz_workshop,biz_event,biz_calendar,cops_head,cops_highlight,cops_workshop,cops_event,cops_calendar,csi_head,csi_highlight,csi_workshop,csi_event,csi_calendar,robo_head,robo_highlight,robo_workshop,robo_event,robo_calendar,sae_head,sae_highlight,sae_workshop,sae_event,sae_calendar


from tinymce.widgets import TinyMCE
from django.db import models

class head_text(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(aero_about_image)
admin.site.register(aero_head,head_text)
admin.site.register(aero_highlight)
admin.site.register(aero_workshop)
admin.site.register(aero_event)
admin.site.register(aero_calendar)

admin.site.register(astro_head)
admin.site.register(astro_highlight)
admin.site.register(astro_workshop)
admin.site.register(astro_event)
admin.site.register(astro_calendar)

admin.site.register(biz_head)
admin.site.register(biz_highlight)
admin.site.register(biz_workshop)
admin.site.register(biz_event)
admin.site.register(biz_calendar)

admin.site.register(cops_head)
admin.site.register(cops_highlight)
admin.site.register(cops_workshop)
admin.site.register(cops_event)
admin.site.register(cops_calendar)

admin.site.register(csi_head)
admin.site.register(csi_highlight)
admin.site.register(csi_workshop)
admin.site.register(csi_event)
admin.site.register(csi_calendar)

admin.site.register(robo_head)
admin.site.register(robo_highlight)
admin.site.register(robo_workshop)
admin.site.register(robo_event)
admin.site.register(robo_calendar)

admin.site.register(sae_head)
admin.site.register(sae_highlight)
admin.site.register(sae_workshop)
admin.site.register(sae_event)
admin.site.register(sae_calendar)




# Register your models here.
