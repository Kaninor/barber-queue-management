from django.db import models


class Barber(models.Model):
    barber_code = models.CharField(max_length=16, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    limit = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BarberHairCut(models.Model):
    barber_code = models.ForeignKey(Barber, on_delete=models.CASCADE)
    personnel_code = models.ForeignKey("personnels.Personnel", on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        ordering = ['-date']
