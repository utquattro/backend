from django.db import models
from django.core.validators import MinValueValidator
from goods.models import Categorie
# Create your models here.


class Promotion(models.Model):
    """"""
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=250, blank=True)
    title = models.TextField(max_length=250, blank=True)
    description = models.TextField(max_length=500, blank=True)
    discount_rate = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1)])
    start_date = models.DateTimeField(verbose_name='дата начала акции')
    end_date = models.DateTimeField(verbose_name='дата завершения акции')
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name


class PromotionCategory(models.Model):
    """"""
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=250, blank=True)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name

