from django.db import models

class Customer(models.Model):
    Full_name = models.CharField(max_length=100)
    Email = models.EmailField()
    Region = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.Full_name
