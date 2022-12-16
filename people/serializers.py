from rest_framework import serializers
from people import models

class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Teachers
        fields = ('id', 'name')
        
class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Students
        fields = ('id', 'name', 'semester')        