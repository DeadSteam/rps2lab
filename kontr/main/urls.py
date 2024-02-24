from django.urls import path
from . import views

# Определяем маршруты URL для вашего приложения
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('input', views.inputs, name='workdb'),
    path('load', views.load, name='loaddb'),
    path('handwork', views.handwork, name='hand'),
    path('indb', views.indb, name='indbwork'),
    path('<int:pk>', views.ArrayDetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.ArrayUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.ArrayDeleteView.as_view(), name='delete')
]
