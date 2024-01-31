from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=100)
    image = models.FileField(upload_to="project_images/", blank=True)
    # id_user = models.IntegerField(null=True)
    persona = models.ForeignKey(
        "Persona",
        on_delete=models.CASCADE,
        null=True,
    )

class Persona(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    c_web = models.CharField(max_length=30)
    c_red1 = models.CharField(max_length=30)
    c_red2 = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30, default="1234")
    image = models.FileField(upload_to="users_images/", blank=True)

class Experiences(models.Model):
    experience = models.TextField()
    persona = models.ForeignKey(
        "Persona",
        on_delete=models.CASCADE,
        null=True,
    )
