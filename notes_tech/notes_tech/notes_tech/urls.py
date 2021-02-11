"""notes_tech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="login"),
    path('home', views.home, name="home"),
    path('profile', views.profile, name="profile"),
    path('feedback', views.feedback, name="feedback"),
    path('sub3rd', views.sub3rd, name="sub3rd"),
    path('sub1st', views.sub1st, name="sub1st"),
    path('sub2nd', views.sub2nd, name="sub2nd"),
    path('b1st', views.b1st, name="b1st"),
    path('n1st', views.n1st, name="n1st"),
    path('v1st', views.v1st, name="v1st"),
    path('p1st', views.p1st, name="p1st"),
    path('register', views.register, name="register"),
    path('userlogout', views.userlogout, name="userlogout"),
    path('home1', views.home1, name="home1"),


]
