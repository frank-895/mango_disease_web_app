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
    re_path(r'^$', views.home, name='home'),
    re_path(r'^diseases/$', views.diseases, name='diseases'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^disease/(?P<name>.+)/$', views.ind_disease, name='ind_disease'),
    re_path(r'^display_record/$', views.display_record, name='display_record'),
    re_path(r'^add_record/$', views.add_record, name='add_record'),
    re_path(r'^account/$', views.account, name='account'),
    re_path(r'^plan/$', views.plan, name='plan'),
    re_path(r'^build/$', views.build, name='build'),
    re_path(r'^record/$', views.record, name='record'),
]