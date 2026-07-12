from django.db import models


class Doctor(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    doctor_id = models.CharField(
        max_length=10,
        unique=True,
        editable=False
    )

    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    qualification = models.CharField(max_length=100)

    experience = models.PositiveIntegerField(
        help_text="Experience in years"
    )

    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    available_from = models.TimeField()
    available_to = models.TimeField()

    address = models.TextField(blank=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="Active"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.doctor_id:
            last = Doctor.objects.order_by("id").last()

            if last:
                number = int(last.doctor_id.split("-")[1]) + 1
            else:
                number = 1

            self.doctor_id = f"DOC-{number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.doctor_id} - {self.full_name}"