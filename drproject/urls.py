"""
URL configuration for drproject project.

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
from django.urls import path
from drproject import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('calcse/', views.cal_view, name='calcse'),
    path('cal1cse/', views.cal1_view, name='cal1cse'),
    path('cal2cse/', views.cal2_view, name='cal2cse'),
    path('cal3cse/', views.cal3_view, name='cal3cse'),
    path('cal4cse/', views.cal4_view, name='cal4cse'),
    path('cal5cse/', views.Book_view, name='cal5cse'),
    path('cal6cse/', views.cal6_view, name='cal6cse'),

]
