from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .models import ToDo

todos_is_progress = ToDo.objects.filter(status='in_progress')

todos_done = ToDo.objects.filter(status='Done')
