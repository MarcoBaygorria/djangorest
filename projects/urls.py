from rest_framework import routers # este modulo nos permite crear las rutas del CRUD
from .api import ProjectViewSet # Importamos el ProjectViewSet

#Ejecutamos el modulo routers
#DefaulRouter() es quien crea EL CRUD
router = routers.DefaultRouter()

#Primero indicamos la ruta ("api/project")
#Despues indicamos el conjunto de datos de ProjectViewSet(api.py)
#Por ultimo ponemos un nombre a la ruta en este caso "projects"

router.register('api/projects', ProjectViewSet, "projects" )

urlpatterns = router.urls

"""
    UNA VEZ hecho las rutas se tendra que agregar a drfsimplecrud/urls.py el projects.urls 
"""
