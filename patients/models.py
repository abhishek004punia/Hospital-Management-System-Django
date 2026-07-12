from django.db import models

# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    patient_id = models.CharField(max_length=20, unique=True, editable=False)
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES)

    mobile = models.CharField(max_length=15)
    email = models.EmailField(blank=True)

    address = models.TextField()

    disease = models.CharField(max_length=100)

    admission_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.patient_id:
            last = Patient.objects.order_by("id").last()

            if last and last.patient_id:
                number = int(last.patient_id.split("-")[1]) + 1
            else:
                number = 1

            self.patient_id = f"PAT-{number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.patient_id} - {self.full_name}"
    
    