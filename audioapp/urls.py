from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('About', views.aboutus, name='about'),
]