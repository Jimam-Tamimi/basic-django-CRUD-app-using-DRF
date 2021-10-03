from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.models import Student

from api.serializers import StudentSerializers 

# Create your views here.
class StudentViewSet(ModelViewSet):
 
    serializer_class = StudentSerializers
    queryset = Student.objects.all()