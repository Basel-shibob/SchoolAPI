from django.shortcuts import render
from rest_framework import viewsets,mixins

from classes import serializers, models
# Create your views here.

class SchoolClassViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SchoolClassSerializer
    queryset = models.SchoolClass.objects.all()

class StudentEnrollmentViewSet(viewsets.ModelViewSet):
    
    """
    A viewset that only handles Create and List 
    for student enrollment in classes.
    """
    serializer_class =  serializers.StudentEnrollmentSerializer
    queryset = models.StudentEnrollment.objects.all()
    