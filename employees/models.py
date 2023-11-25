from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    sick_days = models.IntegerField(default=0)  # Default value set to 0
    start_date = models.DateField()
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.name
