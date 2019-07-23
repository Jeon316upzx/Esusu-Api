
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializer import EsusuGroup_serializer, User_serializer
from .models import EsusuGroup

class userViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_serializer

class groupViewset(viewsets.ModelViewSet):
    queryset = EsusuGroup.objects.all()
    serializer_class = EsusuGroup_serializer
