from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

class head_text(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

    
    
    
    
from .models import aero_head,aero_about_image, aero_highlight,aero_workshop,aero_event

admin.site.register(aero_about_image,head_text)
admin.site.register(aero_head,head_text)
admin.site.register(aero_highlight,head_text)
admin.site.register(aero_workshop,head_text)
admin.site.register(aero_event,head_text)

from .models import astro_head,astro_about_image, astro_highlight,astro_workshop,astro_event

admin.site.register(astro_about_image,head_text)
admin.site.register(astro_head,head_text)
admin.site.register(astro_highlight,head_text)
admin.site.register(astro_workshop,head_text)
admin.site.register(astro_event,head_text)

from .models import biz_head,biz_about_image, biz_highlight,biz_workshop,biz_event

admin.site.register(biz_about_image,head_text)
admin.site.register(biz_head,head_text)
admin.site.register(biz_highlight,head_text)
admin.site.register(biz_workshop,head_text)
admin.site.register(biz_event,head_text)

from .models import csi_head,csi_about_image, csi_highlight,csi_workshop,csi_event

admin.site.register(csi_about_image,head_text)
admin.site.register(csi_head,head_text)
admin.site.register(csi_highlight,head_text)
admin.site.register(csi_workshop,head_text)
admin.site.register(csi_event,head_text)


from .models import cops_head,cops_about_image, cops_highlight,cops_workshop,cops_event

admin.site.register(cops_about_image,head_text)
admin.site.register(cops_head,head_text)
admin.site.register(cops_highlight,head_text)
admin.site.register(cops_workshop,head_text)
admin.site.register(cops_event,head_text)

from .models import robo_head,robo_about_image, robo_highlight,robo_workshop,robo_event

admin.site.register(robo_about_image,head_text)
admin.site.register(robo_head,head_text)
admin.site.register(robo_highlight,head_text)
admin.site.register(robo_workshop,head_text)
admin.site.register(robo_event,head_text)

from .models import sae_head,sae_about_image, sae_highlight,sae_workshop,sae_event

admin.site.register(sae_about_image,head_text)
admin.site.register(sae_head,head_text)
admin.site.register(sae_highlight,head_text)
admin.site.register(sae_workshop,head_text)
admin.site.register(sae_event,head_text)


# Register your models here.
