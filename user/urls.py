from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home),
    path('',views.home),
    path('contactus/',views.contactus),
    path('about/',views.about),
    path('guiderdetails/',views.guiderdetails),
    path('newplaces/',views.newplaces),
    path('signin/',views.signin),
    path('viewdetails/',views.viewdetails),
    path('slider/',views.slider),
    path('gallery/',views.imagegallery),
    path('videos/',views.videogallery),
    path('signin/',views.signin),
]