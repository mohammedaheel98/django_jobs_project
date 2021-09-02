from django.conf.urls import url
from django.urls import path
from testapp import views

urlpatterns = [
    path('home/',views.home_index),
    path('chennai/',views.che_jobs),
    path('hyderabad/',views.hyd_jobs),
    path('bangalore/',views.ban_jobs),
    path('pune/',views.pune_jobs),
]