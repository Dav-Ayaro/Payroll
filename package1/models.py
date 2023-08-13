from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class SpecialUsers(AbstractUser):
    email = models.EmailField(unique=True)
    user_id = models.UUIDField(default=uuid.uuid4,unique=True)

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = uuid.uuid4()
        super(SpecialUsers, self).save(*args, **kwargs)


class Employee(models.Model):
    user = models.OneToOneField(SpecialUsers, on_delete=models.CASCADE, related_name='employee_name')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='payroll_name')
    pay_date = models.DateField()
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)