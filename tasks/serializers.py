from rest_framework import serializers
from .models import Project, Task, Tag

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_at']

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Project name must be at least 3 characters long")
        return value
    

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source='user.username'
    )
    class Meta:
        model = Task
        fields = ['id', 'project', 'title', 'description', 'priority', 'created_at', 'completed', 'tags', 'user']

    def validate_priority(self, value):
        if value not in ['1', '2', '3']:
            raise serializers.ValidationError("Priority must be '1' (High), '2' (Medium), or '3' (Low)")
        return value
    

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']