from django.db import models
import uuid

# Create your models here.

class ClassStreams(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class_title = models.CharField(max_length=54, blank=True, null=True)
    students_number = models.IntegerField(max_length=54, blank=True, null=True)
    teacher = models.CharField(max_length=54, blank=True, null=True)
   
    class Meta:
        db_table = 'class_streams'

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=54, blank=True, null=True)
    admission = models.CharField(max_length=54, blank=True, null=True)
    student_class = models.CharField(max_length=54, blank=True, null=True)

    class Meta:
        db_table = 'student'