from django.db import models
from django.contrib.auth.models import User


class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title


class Submission(models.Model):
    STATUSES = (
        ("canceled", "Qaytarilgan"),
        ("done", "Tasdiqlangan"),
        ("waiting", "Kutilmoqda"),
    )

    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submissions")
    file = models.FileField(upload_to="submissions/")
    submitted_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(choices=STATUSES, max_length=128, default="waiting")

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}"

    def get_badge_class(self):
        return {
            "cancelled": "bg-danger",
            "done": "bg-success",
            "waiting": "bg-primary",
        }[self.status]
