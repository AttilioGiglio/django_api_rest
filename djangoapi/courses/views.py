from django.shortcuts import render
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer

class CourseView(viewsets.ModelViewSet):
    # query to DB, to get all data from table Course DB
    queryset = Course.objects.all()
    # Indicate what serializerclass to use. Change data from python code to JSON data
    serializer_class = CourseSerializer
