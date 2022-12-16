from django.db import models

# Create your models here.
class SchoolClass(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey('people.Teachers', on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

class StudentEnrollment(models.Model):
    student = models.ForeignKey('people.Students', on_delete=models.PROTECT)
    school_class = models.ForeignKey('classes.SchoolClass', on_delete=models.PROTECT)
    semester = models.DateField(auto_now_add=True)