# projects/urls.py

from django.urls import path
from projects import views

urlpatterns = [
    path("<int:pk>/projects/", views.projects, name="projects"),
    path("project/<int:pk>/", views.project_detail, name="project_detail"),
    path("project_new/",views.project_new, name='project_new'),
    path('project_edit/<int:pk>/', views.project_edit, name='project_edit'),
    path("projects/", views.project_index, name="project_index"),
]
