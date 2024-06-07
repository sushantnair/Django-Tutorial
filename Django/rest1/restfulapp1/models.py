from django.db import models

# Create your models here.
class BioData(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    student = models.BooleanField(default=True)
    description = models.TextField()

    def __str__(self):
        return self.first_name

