from django.db import models

# Create your models here.
class Train(models.Model):
    # attributes
    symbol = models.CharField(max_length=1)

class Station(models.Model):
    # attributes
    name = models.CharField(max_length=30)

    # relations
    trains = models.ManyToManyField(Train)

class Destination(models.Model):
    # attributes
    name = models.CharField(max_length=30)

class Trip(models.Model):
    # attributes
    date = models.DateField()
    duration = models.IntegerField()
    departure = models.TimeField()
    arrival = models.TimeField()

    # relations
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    train_0 = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='train_0')
    train_1 = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='train_1')
    train_2 = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='train_2')
    

