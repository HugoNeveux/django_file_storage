"""Django_webdav_tests URL Configuration

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
from django.urls import path, include
import Files, Auth, Settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Files/', include('Files.urls'), name='Files'),
    path('', include('Auth.urls'), name='Auth'),
    path('Settings/', include('Settings.urls'), name='Settings'),
    path('Share/', include('Share.urls'), name='Share'),
]
