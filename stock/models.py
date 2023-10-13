from django.db import models
from django.core.validators import MinValueValidator
from goods.models import ProductSku
# Create your models here.


class Warehouse(models.Model):
    """"""
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=250, blank=True, verbose_name='Название склада')
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание склада')
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name




