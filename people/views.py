from django.shortcuts import render
from rest_framework import viewsets

from people import serializers, models
# Create your views here.

class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TeacherSerializer
    queryset = models.Teachers.objects.all()
    
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Students.objects.all()    