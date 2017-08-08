"""muypicky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from restaurants.views import restaurant_listview

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#    # Cara pemanggilan template seperti dibawah ini merupakan cara jika kita mempunya context view
#    # Yang akan ditambahkan pada template tampilan kita dan itu di edit di views.py
#    url(r'^$', HomeView.as_view()),
    url(r'^resto/$', restaurant_listview),
    
    # Cara seperti dibawah ini merupakan cara pemanggilan template secara langsung
    # Dikarenakan kita tidak mempunya centext view yang ingin ditambahkan pada tamplate view
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^about-page/$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact-page/$', TemplateView.as_view(template_name='contact.html')),
]
