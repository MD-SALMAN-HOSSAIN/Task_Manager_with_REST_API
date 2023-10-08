from rest_framework import serializers
from .models import Task, TaskPhoto

class TaskPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPhoto
        fields = ['id', 'photo','task']

class TaskSerializer(serializers.ModelSerializer):
    photos = TaskPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'creation_datetime', 'due_date', 'priority', 'complete', 'user', 'photos']
