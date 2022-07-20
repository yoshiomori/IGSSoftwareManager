from django.db import models


class Departament(models.Model):
    name = models.CharField(max_length=255)


class Employ(models.Model):
    name = models.CharField(max_length=747)  # largest name 747 Ref.: https://www.guinnessworldrecords.com/world-records/67285-longest-personal-name#:~:text=The%20longest%20personal%20name%20is,verified%20on%201%20January%202021.
    email = models.EmailField()
    departament = models.ForeignKey(Departament, models.SET_NULL, null=True)  # The registry of employ will stay even when departament has been deleted

    class Meta:
        verbose_name_plural = "Employees"
