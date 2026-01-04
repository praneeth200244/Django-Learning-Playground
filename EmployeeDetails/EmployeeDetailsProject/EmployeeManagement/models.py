from django.db import models

class Employee(models.Model):
    # Name fields
    firstName = models.CharField(max_length=128)
    middleName = models.CharField(max_length=128, blank=True, null=True)
    lastName = models.CharField(max_length=128)

    # Gender choices
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    # Photo
    photo = models.ImageField(upload_to='employeeImages/', blank=True, null=True)

    # Contact info
    mobileNumber = models.CharField(max_length=15, blank=True, null=True)
    emailAddress = models.EmailField(unique=True)

    # Designation choices
    DESIGNATION_CHOICES = [
        ('Associate Software Engineer', 'Associate Software Engineer'),
        ('Software Engineer', 'Software Engineer'),
        ('Senior Software Engineer', 'Senior Software Engineer'),
        ('Staff Software Engineer', 'Staff Software Engineer'),
        ('Senior Staff', 'Senior Staff'),
        ('Principal Engineer', 'Principal Engineer'),
        ('Senior Principal Engineer', 'Senior Principal Engineer'),
        ('Distinguished Engineer', 'Distinguished Engineer'),
    ]

    designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES)


    # Timestamps
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.emailAddress}"

