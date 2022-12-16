from rest_framework import serializers

from classes import models

class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SchoolClass
        fields = ('id', 'name', 'teacher')
        
        
class StudentEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentEnrollment
        fields = ('id', 'student', 'school_class', 'semester')