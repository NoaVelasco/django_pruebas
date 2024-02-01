from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=100)
    image = models.FileField(upload_to="project_images/", blank=True)
    persona = models.ForeignKey(
        "Persona",
        on_delete=models.CASCADE,
        null=True,
    )


class Persona(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    web = models.URLField(blank=True)
    rrss_1 = models.URLField(blank=True)
    rrss_2 = models.URLField(blank=True)
    # c_web = models.CharField(max_length=30)
    # c_red1 = models.CharField(max_length=30)
    # c_red2 = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30, default="1234")
    image = models.FileField(upload_to="users_images/", blank=True)


class Experience(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    company = models.CharField(max_length=40, blank=True, null=True)
    # @TODO: ¿cómo se ordena en función de la fecha más reciente de fin+ini?
    init_date = models.DateField(null=True, blank=True)
    # @TODO: ¿Tendría que ser un string para dar la opción de poner "en la actualidad"?
    end_date = models.DateField(null=True, blank=True)
    experience = models.TextField(
        help_text="Describe tu cargo y funciones."
    )
    # @TODO: Para el panel de admin, ¿se puede mostrar el nombre y no el id de Persona?
    persona = models.ForeignKey(
        "Persona",
        on_delete=models.CASCADE,
        null=True,
    )
