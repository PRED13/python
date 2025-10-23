from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('interpreter/', views.predict_survival, name='predict_survival'),
]
