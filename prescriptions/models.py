from django.db import models
from doctors.models import Doctor
from patients.models import Patient
from appointments.models import Appointment


class Prescription(models.Model):

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Completed", "Completed"),
    ]

    prescription_id = models.CharField(
        max_length=10,
        unique=True,
        editable=False
    )

    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    medicine = models.CharField(max_length=200)

    dosage = models.CharField(max_length=100)

    duration = models.CharField(max_length=100)

    instructions = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        if not self.prescription_id:

            last = Prescription.objects.order_by("id").last()

            if last:
                number = int(last.prescription_id.split("-")[1]) + 1
            else:
                number = 1

            self.prescription_id = f"PRE-{number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.prescription_id} - {self.patient.full_name}"