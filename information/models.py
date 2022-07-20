from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)  # It would be weird if there are two department with same name

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=747)  # largest name 747 Ref.: https://www.guinnessworldrecords.com/world-records/67285-longest-personal-name#:~:text=The%20longest%20personal%20name%20is,verified%20on%201%20January%202021.
    email = models.EmailField(unique=True)  # unique email by employee allow to identify an employ by email
    department = models.ForeignKey(Department, models.SET_NULL, null=True)  # The registry of employ will stay even when departament has been deleted

    def __str__(self):
        return self.name
