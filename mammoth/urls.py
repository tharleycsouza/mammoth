"""mammoth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from barman import views

admin.site.site_title = 'Mammoth Admin'
admin.site.site_header = 'Mammoth Admin'
admin.site.index_title = 'Mammoth Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django-sb-admin/', include('django_sb_admin.urls')),
    path('', views.dashboard, name='dashboard'),
    path('', views.pg_register, name='pg_register'),

]


