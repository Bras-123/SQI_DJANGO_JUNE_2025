from django.urls import path

from . import views
urlpatterns=[
    path('extras/', views.aboutus, name='about_us'),
    
]