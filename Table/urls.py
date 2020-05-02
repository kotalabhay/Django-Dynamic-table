"""Table URL Configuration

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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from DynamicTable import views

urlpatterns  = [
    path('admin/', admin.site.urls),
    path('', views.HomePage,name="home"),
    path('/insert_details', views.insert,name="insert"),
    path('/update_details', views.update_details,name="update_details"),
    path('/delete_details', views.delete_details,name="delete_details"),
    path('insert_table', views.insert_table,name="insert_table"),



]
