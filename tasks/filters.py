from django_filters import rest_framework as filters
from .models import Task

class TaskFilter(filters.FilterSet):
    title = filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
    )
    priority = filters.ChoiceFilter(choices=Task.PRIORITY_CHOICES)
    completed = filters.BooleanFilter()

    class Meta:
        model = Task
        fields = ['title', 'priority', 'project', 'completed']