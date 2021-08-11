from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    pass


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="patient")

    def __str__(self) -> str:
        return f"{self.id}: {self.user.name} {self.user.last_name}"


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctor")

    def __str__(self) -> str:
        return f"{self.id}: {self.user.name} {self.user.last_name}"


class Checkup(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="checkups"
    )
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name="checkups"
    )
    file = models.FileField(upload_to="/files")
    note = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Checkup {self.id}: {self.doctor.user.name} {self.doctor.user.last_name} -> {self.patient.user.name} {self.patient.user.last_name}"
