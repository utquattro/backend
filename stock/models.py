from django.db import models
from django.core.validators import MinValueValidator
from goods.models import ProductSku
# Create your models here.


class Warehouse(models.Model):
    """"""
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=250, blank=True)
    description = models.TextField(max_length=500, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name


class WarehouseAmount(models.Model):
    """"""
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    stock = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product_item = models.ForeignKey(ProductSku, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    class Meta:
        unique_together = ('stock', 'product_item')

