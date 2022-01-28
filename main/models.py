from django.db import models


# Create your models here.


class Item(models.Model):

    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    buy_date = models.DateTimeField()
    location = models.CharField(max_length=50)

    @property
    def getPrice(self):
        return str(self.retail_price)

    def getName(self):
        return str(self.name)

    def __str__(self):
        return self.name
