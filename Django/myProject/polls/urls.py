from django.urls import path
from . import views

urlpatterns = [ # This is a list of paths
    path('', views.home, name='home'),
    path('tourist_attractions/', views.tourist_attractions, name='tourist_attractions'),
]
