from django.db import models
from accounts.models import User
from stocks.models import Product

class Sales(models.Model):
    name = models.CharField(max_length=50,unique=True)
    item = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    unit_price = models.FloatField(verbose_name='unit price')
    total_amount = models.IntegerField(verbose_name='total amount')
    sold_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    sold_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a string representation of this sale."""
        return self.name