from rest_framework import serializers
from .models import Project

# ----------------------- Creamos una class para hacer consultas a una BBDD ---------------------- #

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "title", "description", "technology", "created_at") # Campos de la tabla
        read_only_fields = ("created_at", ) # campo de solo lectura, no se puede modificar.