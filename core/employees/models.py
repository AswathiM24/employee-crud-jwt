from django.db import models
from django.core.exceptions import ValidationError


class Employee(models.Model):
    name = models.TextField()
    department = models.TextField()
    salary = models.IntegerField()
    joining_date = models.DateField()

    def save(self, *args, **kwargs):
        if self.salary < 0:
            raise ValidationError({'salary': 'Salary must not be negative.'})
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

