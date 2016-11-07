from django.conf.urls import include, url
from django.contrib import admin

from main_page import views

urlpatterns = [
    url(r'^new/', views.new_ad, name = 'new_ad'),
    url(r'^current/(?P<ad_id>\d+)', views.show_current, name = 'show_current'),
    url(r'^', views.show_billboard, name = 'show_billboard'),
]