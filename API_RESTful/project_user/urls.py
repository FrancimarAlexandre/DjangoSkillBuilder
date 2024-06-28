
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.models import User
from rest_framework import routers
from api import views 





# Routers fornecem uma maneira fácil de determinar  automaticamente a configuração do URL

router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet) 
router.register(r'groups',views.GroupViewSet) 
urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls') ,name='rest_framework')
]
