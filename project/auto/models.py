from django.db import models


class Auto(models.Model):
    brand = models.CharField(max_length=100) # Бренд автомобиля-
    model = models.CharField(max_length=100) # Модель автомобиля
    year = models.IntegerField() # Год выпуска
    color = models.CharField(max_length=50) #Цвет

    def str(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.color}"