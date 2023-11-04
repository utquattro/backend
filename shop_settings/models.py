from django.db import models
from django_project.base_model import BaseModel, ImgModel


class Information(BaseModel):
    class Position(models.TextChoices):
        copyright = "copyright"
        phone_main = "phone_main"
        phone_second = "phone_second"

    name = models.CharField(choices=Position.choices, unique=True, null=True)
    value = models.TextField(verbose_name='Значение')
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Logo(ImgModel):
    """"""
    img_url = models.ImageField(upload_to='images/shop_settings/logo')


class PaySystem(ImgModel):
    """"""
    name = models.TextField(verbose_name='Платежная система')
    img_url = models.ImageField(upload_to='images/shop_settings/pay_system')


class Socical(ImgModel):
    """"""
    name = models.TextField(verbose_name='Название соц.сети')
    description= models.TextField(verbose_name='ссылка на соц.сеть')
    img_url = models.ImageField(upload_to='images/shop_settings/social')


class MarketingBanner(ImgModel):
    """"""
    name = models.TextField(verbose_name='Имя баннера')
    img_url = models.ImageField(upload_to='images/shop_settings/marketing_banner')
