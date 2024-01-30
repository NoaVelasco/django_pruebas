from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    exp1 = models.TextField()
    exp2 = models.TextField()
    exp3 = models.TextField()
    c_web = models.CharField(max_length=30)
    c_red1 = models.CharField(max_length=30)
    c_red2 = models.CharField(max_length=30)
    c_email = models.CharField(max_length=30)
    image = models.FileField(upload_to="users_images/", blank=True)
