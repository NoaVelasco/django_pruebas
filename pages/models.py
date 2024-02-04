from django.db import models

# Create your models here.

# @NOA: Estos modelos ya estaban creados en Projects. Sé que no era el lugar adecuado,
# pero no he podido trasladarlos a Pages sin que me salgan errores de migración.
# Ahora, estos modelos están duplicados y no sirven, pero tampoco puedo borrarlos.
class Persona(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    web = models.URLField(blank=True)
    rrss_1 = models.URLField(blank=True)
    rrss_2 = models.URLField(blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=30, default="1234")
    image = models.FileField(upload_to="users_images/", blank=True)


class Experience(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    company = models.CharField(max_length=40, blank=True, null=True)
    # @TODO: ¿cómo se ordena en función de la fecha más reciente de fin+ini?
    init_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    experience = models.TextField(help_text="Describe tu cargo y funciones.")
    persona = models.ForeignKey(
        "Persona",
        on_delete=models.CASCADE,
        null=True,
    )
