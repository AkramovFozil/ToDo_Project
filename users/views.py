from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from .models import User, ToDo
from .serializers import EmailTokenObtainPairSerializer, UserRegistrationSerializers, ToDoSerializers


class UserSignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializers


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


class ToDoView(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers
