from rest_framework import viewsets, permissions
from .models import Todos
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todos.objects.all()
    permission_class = [
        permissions.AllowAny
    ]

    serializer_class = TodoSerializer