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
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # MAIN NAVIGATION PATHS
    re_path(r'^$', views.home, name='home'),
    re_path(r'^diseases/$', views.diseases, name='diseases'),
    re_path(r'^about/$', views.about, name='about'),
    path('disease/<str:name>/', views.ind_disease, name='ind_disease'),
    
    # ORCHARD PATHS
    path('add_orchard/', views.add_orchard, name='add_orchard'),
    path('orchard/edit/<int:orchard_id>/', views.edit_orchard, name='edit_orchard'),
    path('orchard/delete/<int:orchard_id>/', views.delete_orchard, name='delete_orchard'),
    path('orchards/', views.orchard_list, name='orchard_list'),
    
    # USER AUTHENTICATION PATHS
    path('userlogin/', views.userlogin, name="userlogin"),
    path('register/', views.register, name="register"),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='mango_disease_app/password_reset.html'), name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='mango_disease_app/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='mango_disease_app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='mango_disease_app/password_reset_complete.html'), name='password_reset_complete'),
    re_path(r'^account/$', views.account, name='account'),
    
    # CASES PATHS
    path('cases/records/<int:case_id>/', views.records, name='records'),
    path('cases/add_record/<int:case_id>/', views.add_record, name='add_record'),
    
    # RECORDS PATHS
    re_path(r'^cases/$', views.cases, name='cases'),
    re_path(r'^new_case/$', views.new_case, name='new_case'),
    
    # DISEASE PATHS
    re_path(r'^add_disease/$', views.add_disease, name='add_disease'),
    path('disease/edit/<int:disease_id>/', views.edit_disease, name='edit_disease'),
    path('disease/delete/<int:disease_id>/', views.delete_disease, name='delete_disease'),
    
    # LOCATION PATHS
    re_path(r'^add_location/$', views.add_location, name='add_location'),
    path('location/edit/<int:location_id>/', views.edit_location, name='edit_location'),
    path('location/delete/<int:location_id>/', views.delete_location, name='delete_location'),   
    
    # VARIETY PATHS
    re_path(r'^add_variety/$', views.add_variety, name='add_variety'),
    path('variety/edit/<int:variety_id>/', views.edit_variety, name='edit_variety'),
    path('variety/delete/<int:variety_id>/', views.delete_variety, name='delete_variety'),   
        
    # OTHER ACCOUNT PATHS
    re_path(r'^plan/$', views.plan, name='plan'),
    re_path(r'^admintools/$', views.admin_tools, name='admin_tools'),
    path('custom-admin/add/', views.add_admin, name='add_admin'),
    path('custom-admin/edit/<int:admin_id>/', views.edit_admin, name='edit_admin'),
    path('custom-admin/delete/<int:admin_id>/', views.delete_admin, name='delete_admin'),   

]

# Code from https://how.dev/answers/how-to-upload-images-in-django
# This is because Django does not servce media files by default in development. 
# It instructs Django to serve files from /media/ to be viewed in the browser.
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
