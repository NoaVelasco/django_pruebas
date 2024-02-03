from django.urls import path
from pages import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.bio, name="bio"),
    path("<int:pk>/bio_edit/", views.bio_edit, name="bio_edit"),
    path("<int:pk>/exp/", views.exp, name="exp"),
    # path("", views.home, name="home"),
    path("home_edit/", views.home_edit, name="home_edit"),
    path("experience/", views.experience, name="experience"),
    path("experience_edit/<int:pk>", views.experience_edit, name="experience_edit"),
]
