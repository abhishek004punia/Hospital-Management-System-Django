from django.db import models

from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment


class Billing(models.Model):

    PAYMENT_STATUS = [
        ("Paid", "Paid"),
        ("Pending", "Pending"),
    ]

    bill_id = models.CharField(
        max_length=20,
        unique=True
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE
    )

    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    medicine_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    test_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    other_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="Pending"
    )

    bill_date = models.DateField()

def save(self, *args, **kwargs):

    self.total_amount = (
        self.consultation_fee +
        self.medicine_charge +
        self.test_charge +
        self.other_charge
    )

    super().save(*args, **kwargs)

def __str__(self):
    return self.bill_id