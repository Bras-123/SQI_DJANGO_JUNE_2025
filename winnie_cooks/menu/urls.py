from django.urls import path

from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.availabe_dishes, name = 'available_dishes')
]