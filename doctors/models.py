from django.db import models


class Doctor(models.Model):

    doctor_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    experience = models.IntegerField()
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    joining_date = models.DateField()

    def __str__(self):
        return self.full_name