"""sntc_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'clubs'


urlpatterns = [
    path("aero/", views.aero, name = 'Aero-Modelling Club'),
    path("astro/", views.astro, name = 'Astronomy Club'),
    path("biz/", views.biz, name = 'Business Club'),
    path("csi/", views.csi, name = 'Club of Sustainibility and Innovation'),
    path("cops/", views.cops, name = 'Club of Programmers'),
    path("robo/", views.robo, name = 'Robotics Club'),
    path("sae/", views.sae, name = 'Society of Automotive Engineers'),

    path('admin/', admin.site.urls),
]
