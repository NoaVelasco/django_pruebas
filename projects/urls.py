# projects/urls.py

from django.urls import path
from projects import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("new/",views.project_new, name='project_new'),
    path('<int:pk>/edit/', views.project_edit, name='project_edit'),
]
