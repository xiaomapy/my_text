"""BMS URL Configuration

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
from BookManageSystem import views

urlpatterns = [
    #图书url
    url(r'^book_list/', views.book_list),
    url(r'^add_book/', views.add_book),
    url(r'^del_book/', views.del_book),
    url(r'^eid_book/', views.eid_book),
    #当前时间url
    url(r'^timer/', views.timer),
    #出版社url
    url(r'^publisher_list', views.publisher_list)

]
