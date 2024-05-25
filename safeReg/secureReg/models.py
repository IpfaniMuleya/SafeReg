from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=255, blank=True)
    institution = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username

class Module(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255, blank=True)
    duration = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    instructors = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='pending')

    def __str__(self):
        return f"{self.user.username} - {self.module.title}"
