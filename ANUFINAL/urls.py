"""
URL configuration for ANUFINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from NUTRIANU import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="Home"),
    path('client', views.client,name="client"),
    path('login', views.login,name="login"),
    path('login2', views.login2,name="login2"),
    path('form/', views.form,name="form"),
    path('form/important', views.important,name="important"),
    path('aboutus/', views.aboutus,name="aboutus"),
    path('tips/', views.tips,name="tips"),
    path('error/', views.error,name="error"),
    path('final', views.final,name="final"),
    path('diet3', views.diet3,name="diet3"),
    path('normal', views.normal,name="normal"),
    path('clientdetails', views.clientdetails,name="clientdetails"),
    path('pages', views.pages,name="pages"),
    path('update', views.update,name="update"),
    path('high', views.high,name="High"),
    path('weightloss', views.weightloss,name="weightloss"),
    path('weightgain', views.weightgain,name="weightgain"),
    path('diabetic', views.high,name="diabetic"),
    path('video/', views.video,name="video"),
    path('video2dia/', views.video2dia,name="video2dia"),
    path('videochol/', views.videochol,name="videochol"),
    path('videoweightgai/', views.videoweightgai,name="videoweightgai"),
    path('videoweightloss/', views.videoweightloss,name="videoweightloss"),
   
    
]
