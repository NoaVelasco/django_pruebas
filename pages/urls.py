from django.urls import path
from pages import views

urlpatterns = [
    path("<int:pk>", views.home, name="home"),
    path("<int:pk>/experience", views.experience, name="experience"),
    # @NOA: Creo que es redundante meter estos paths aquí también.
    # Ya están en urls.py del proyecto principal.
    # path("projects", views.projects, name="projects"),
]
