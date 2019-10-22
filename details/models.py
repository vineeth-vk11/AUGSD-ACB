from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_email = models.EmailField(
        verbose_name='Student email',
        max_length=255,
        unique=True,
        default='NIL'
    )
    father_email = models.EmailField(
        verbose_name='Father email',
        max_length=255,
        unique=True,
        default='NIL'
    )
    mother_email = models.EmailField(
        verbose_name='Mother email',
        max_length=255,
        unique=True,
        default='NIL'
    )
    student_contact = models.CharField(max_length=10, default='NIL')
    father_contact = models.CharField(max_length=10, default='NIL')
    mother_contact = models.CharField(max_length=10, default='NIL')

    address = models.CharField(max_length=10000, default='NIL')

    def __str__(self):
        return self.user.username


class score(models.Model):
    User = get_user_model()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Student")
    subject_name = models.CharField(max_length=30, default='NIL')
    midsem_grade = models.CharField(max_length=15, default='NIL')
    midsem_score = models.CharField(max_length=20, default='NIL')
    attendance = models.CharField(max_length=20, default='NIL')

    def __str__(self):
        return f"{self.user.username} - {self.subject_name}"


class attendance(models.Model):
    User = get_user_model()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attendance")
    subject_name = models.CharField(max_length=20, default='NIL')
    classes = models.CharField(max_length=20, default="NIL")
    attended = models.CharField(max_length=20, default='NIL')
    percentage = models.CharField(max_length=20, default='NIL')

    def __str__(self):
        return f"{self.user.username}-{self.subject_name}"
