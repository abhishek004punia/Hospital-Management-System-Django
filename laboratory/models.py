from django.db import models


class LabTest(models.Model):

    test_id = models.AutoField(primary_key=True)

    patient_name = models.CharField(max_length=100)

    doctor_name = models.CharField(max_length=100)

    test_name = models.CharField(max_length=100)

    test_date = models.DateField()

    result = models.CharField(max_length=100)

    charges = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.test_name