from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField('Name', max_length=20, null=False, blank=False)
    class_no = models.CharField('Class', max_length=5, null=False, blank=False)
    section = models.CharField('Section', max_length=5, null=False, blank=False)
    def __str__(self):
        return self.name