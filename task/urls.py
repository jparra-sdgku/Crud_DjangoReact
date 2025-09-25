from django.urls import include, path
from rest_framework import routers
from . import views





# Routers api versioning

router = routers.DefaultRouter()
router.register(r'tasks',views.TaskView, 'tasks')




urlpatterns = [
    path('api/v1/',include(router.urls) ),
   

]

#GET POST, update, delete