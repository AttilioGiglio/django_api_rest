from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    # self = Course model and passing name to admin
    def __str__(self):
        return self.name 
