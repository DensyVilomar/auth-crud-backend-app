from .models import Task
from .serializers import TaskSerializer

from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class TaskListApiView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user.id

        tasks = Task.objects.filter(creator=user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = TaskSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailApiView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        data = request.data
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        data = request.data
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        task = Task.objects.get(id=id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
