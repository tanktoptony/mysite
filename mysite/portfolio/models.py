from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="projects")
    description = models.TextField()
