from django.db import models

# --- Creacion de una tabla en la base de datos que este conectada a django -- #
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
