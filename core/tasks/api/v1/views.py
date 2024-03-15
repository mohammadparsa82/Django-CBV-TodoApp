from django.shortcuts import get_object_or_404
from tasks.models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

class TaskList(APIView):
    # getting a list of tasks and creating new tasks
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TaskSerializer

    def get(self,request):
        tasks = Task.objects.all()
        serializers = TaskSerializer(tasks,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializers = TaskSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
    

class TaskDetail(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get(self,request,id):
        tasks = get_object_or_404(Task,pk=id)
        serializers = TaskSerializer(tasks)
        return Response(serializers.data)
    def put(self,request,id):
        task = get_object_or_404(Task,pk=id)
        serializers = TaskSerializer(task,data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
    def delete(self,request,id):
        task = get_object_or_404(Task,pk=id)
        task.delete()
        return Response({"detail":"item removed successful"},status=status.HTTP_204_NO_CONTENT)