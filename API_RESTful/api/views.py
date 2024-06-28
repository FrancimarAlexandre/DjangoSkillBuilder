from django.shortcuts import render
from rest_framework import viewsets,permissions
from .serializers import UserSerializer,GroupSerializer
from django.contrib.auth.models import Group,User
# Create your views here.
# ViewSets define o comportamento da view
class UserViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os usuários sejam visualizados ou editados.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que grupos sejam visualizados ou editados.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_class = [permissions.IsAuthenticated]
