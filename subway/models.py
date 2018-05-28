from django.db import models

# Create your models here.
class Train(models.Model):
    # attributes
    symbol = models.CharField(max_length=1)

    # functions
    def __str__(self):
        return self.symbol

class Station(models.Model):
    # attributes
    name = models.CharField(max_length=30)

    # relations
    trains = models.ManyToManyField(Train)

    # functions
    def __str__(self):
        return self.name

class Destination(models.Model):
    # attributes
    name = models.CharField(max_length=30)

    # functions
    def __str__(self):
        return self.name

class Trip(models.Model):
    # attributes
    date = models.DateField()
    duration = models.IntegerField()
    departure = models.TimeField()
    arrival = models.TimeField()

    # relations
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    train_0 = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='train_0')
    train_1 = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='train_1', blank=True, null=True)
    train_2 = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='train_2', blank=True, null=True)
    
    # functions
    def __str__(self):
        return "{} - {}".format(self.date, self.destination.name)
