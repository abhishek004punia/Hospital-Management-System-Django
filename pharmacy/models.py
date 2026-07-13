from django.db import models


class Medicine(models.Model):

    medicine_id = models.AutoField(primary_key=True)

    medicine_name = models.CharField(max_length=100)

    manufacturer = models.CharField(max_length=100)

    category = models.CharField(max_length=100)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.PositiveIntegerField()

    expiry_date = models.DateField()

    description = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.medicine_name