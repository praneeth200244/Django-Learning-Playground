from datetime import date
from django.db import models


class Employee(models.Model):

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employee"

    class Designation(models.TextChoices):
        ASSOCIATE_SW_APPLICATIONS_ENGINEER = (
            "Associate SW Applications Engineer",
            "Associate SW Applications Engineer",
        )
        SW_APPLICATIONS_ENGINEER = (
            "SW Applications Engineer",  # Value stored in the database
            "SW Applications Engineer",  # Label displayed in Django admin
        )
        SR_SW_APPLICATIONS_ENGINEER = (
            "SR SW Applications Engineer",
            "SR SW Applications Engineer",
        )
        STAFF_SW_APPLICATIONS_ENGINEER = (
            "Staff SW Applications Engineer",
            "Staff SW Applications Engineer",
        )
        PRINCIPAL_SW_APPLICATIONS_ENGINEER = (
            "Principal SW Applications Engineer",
            "Principal SW Applications Engineer",
        )
        SR_PRINCIPAL_SW_APPLICATIONS_ENGINEER = (
            "SR Principal SW Applications Engineer",
            "SR Principal SW Applications Engineer",
        )
        DISTINGUISHED_ENGINEER = (
            "Distinguished Engineer",
            "Distinguished Engineer",
        )
        SR_DISTINGUISHED_ENGINEER = (
            "SR Distinguished Engineer",
            "SR Distinguished Engineer",
        )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    designation = models.CharField(
        max_length=100,
        choices=Designation.choices
    )

    date_of_birth = models.DateField(
        verbose_name="Date of Birth"
    )

    date_of_joining = models.DateField()

    photo = models.ImageField(
        upload_to="employee_photos/"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(
        blank=True,
        null=True
    )

    @property
    def age(self):
        today = date.today()
        dob = self.date_of_birth

        return (
            today.year - dob.year
            - ((today.month, today.day) < (dob.month, dob.day))
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"