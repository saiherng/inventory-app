from django.db import models
#from djmoney.models.fields import MoneyField


# Create your models here.


class Item(models.Model):

    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    buy_date = models.DateTimeField()

    @property
    def getPrice(self):
        return str(self.retail_price) + " Kyats"

    def __str__(self):
        return self.name
