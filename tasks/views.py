from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
def home(request):
    return HttpResponse("Welcome to the Task API! Visit /api/tasks/ to see tasks.")

# Create your views here.
