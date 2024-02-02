from django.urls import path
from pages import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.home, name="home"),
   # path("projects", views.projects, name="projects"),
    path("experience", views.experience, name="experience"),
=======
    path("<int:pk>", views.home, name="home"),
    path("<int:pk>/experience", views.experience, name="experience"),
    # @NOA: Creo que es redundante meter estos paths aquí también.
    # Ya están en urls.py del proyecto principal.
    # path("projects", views.projects, name="projects"),
>>>>>>> 4db0e225bfb33b97bc6fd4bf0f12b4ce03fde929
]
