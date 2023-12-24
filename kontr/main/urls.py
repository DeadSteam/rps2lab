from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('input', views.inputs, name='workdb'),
    path('load', views.load, name='loaddb'),
    path('handwork', views.handwork, name='hand'),
    path('autowork', views.autowork, name='auto'),
]
