from rest_framework import viewsets, permissions, pagination, filters as drf_filters
from django_filters import rest_framework as filters
from .models import Project, Task, Tag
from .serializers import ProjectSerializer, TaskSerializer, TagSerializer
from .filters import TaskFilter


# Project viewset
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

# Pagination Custom Class
class CustomPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

# Tasks View
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination

    # Filters 
    filter_backends = [filters.DjangoFilterBackend, drf_filters.SearchFilter]
    filterset_class = TaskFilter
    search_fields = ['title', 'priority', 'completed']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()