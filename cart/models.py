from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from datetime import datetime
from django_project.base_model import BaseModel
from goods.models import ProductSku


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductSku, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, blank=False)
