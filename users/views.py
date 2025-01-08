from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView

from .models import User
from .serializers import EmailTokenObtainPairSerializer, UserRegistrationSerializers


class UserSignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializers


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer
