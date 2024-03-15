from rest_framework import serializers
from tasks.models import * 

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'user',
            'id',
            'title',
            'complete',
            'created_date',
            'updated_date',
        ]