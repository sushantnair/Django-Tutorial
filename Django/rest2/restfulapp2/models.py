from django.db import models

# Create your models here.

# PART A

'''
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    student = models.BooleanField()
    # True => student; False => alumni
    description = models.TextField()
'''

# PART B

class Courses(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=8)
    certificate = models.BooleanField()
    course_duration = models.TimeField()
    course_domain = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    student = models.BooleanField()
    description = models.TextField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, 
                                related_name='courses', null=True, blank=True)

