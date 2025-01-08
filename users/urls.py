from django.urls import path
from .views import EmailTokenObtainPairView, UserSignUpView
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('login/', EmailTokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('register/', UserSignUpView.as_view(), name='register'),
]
