from django.db import models


class Personnel(models.Model):
    personnel_code = models.CharField(max_length=16, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PersonnelWaiting(models.Model):
    personnel_code = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    barber_code = models.ForeignKey("barbers.Barber", on_delete=models.CASCADE)
    reserved_date = models.DateField()

    class Meta:
        ordering = ['-reserved_date']
