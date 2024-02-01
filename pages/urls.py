from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name="home"),

    # @NOA: Creo que es redundante meter estos paths aquí también.
    # Ya están en urls.py del proyecto principal.
    # path("projects", views.projects, name="projects"),
    # path("experience", views.experience, name="experience"),
]
