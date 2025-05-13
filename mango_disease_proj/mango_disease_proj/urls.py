"""
URL configuration for mango_disease_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, re_path
from mango_disease_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name="register"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('add_orchard/', views.add_orchard, name='add_orchard'),
    path('orchard/edit/<int:orchard_id>/', views.edit_orchard, name='edit_orchard'),
    path('orchard/delete/<int:orchard_id>/', views.delete_orchard, name='delete_orchard'),
    path('orchards/', views.orchard_list, name='orchard_list'),

    
    re_path(r'^$', views.home, name='home'),
    re_path(r'^diseases/$', views.diseases, name='diseases'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^disease/(?P<name>.+)/$', views.ind_disease, name='ind_disease'),

    re_path(r'^add_record/$', views.add_record, name='add_record'),
    re_path(r'^account/$', views.account, name='account'),
    re_path(r'^admintools/$', views.admin_tools, name='admin_tools'),
    re_path(r'^add_disease/$', views.add_disease, name='add_disease'),
    re_path(r'^add_location/$', views.add_location, name='add_location'),
    re_path(r'^add_variety/$', views.add_variety, name='add_variety'),
    re_path(r'^plan/$', views.plan, name='plan'),
    re_path(r'^build/$', views.build, name='build'),
]

# Code from https://how.dev/answers/how-to-upload-images-in-django
# This is because Django does not servce media files by defauly in development. 
# It instructs Django to serve files from /media/ to be viewed in the browser.
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)