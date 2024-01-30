from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name="home"),
    path("projects", views.projects, name="projects"),
    path("experience", views.experience, name="experience"),
]
