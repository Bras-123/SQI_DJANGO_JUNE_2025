from django.urls import path

from . import views
urlpatterns=[
    path('gadgets/', views.gadgets_we_have, name='gadgets'),
    
]