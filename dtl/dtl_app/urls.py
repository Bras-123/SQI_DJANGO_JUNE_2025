from django.urls import path

from . import views

urlpatterns = [
    path ('messages', views.practice_dtl, name = 'dtl_practise')
]


