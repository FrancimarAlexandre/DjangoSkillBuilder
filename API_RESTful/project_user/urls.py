
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.models import User
from rest_framework import routers,serializers,viewsets  


# Serializer define a  representação da api
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','is_staff']

# ViewSets define o comportamento da view
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers fornecem uma maneira fácil de determinar  automaticamente a configuração do URL

router = routers.DefaultRouter()
router.register(r'users',UserViewSet) 
urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls') ,name='rest_framework')
]
