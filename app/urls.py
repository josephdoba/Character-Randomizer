from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('generate_character/', views.generate_character_ajax, name='generate_character_ajax')
]