from django.urls import path, include
from .views import EmailTokenObtainPairView, UserSignUpView, ToDoView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('todo', ToDoView)

urlpatterns = [
    path('login/', EmailTokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('register/', UserSignUpView.as_view(), name='register'),
    path('', include(router.urls)),

]
