from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=20)
    image = models.FileField(upload_to="project_images/", blank=True)
    id_user = models.IntegerField(null=True)
