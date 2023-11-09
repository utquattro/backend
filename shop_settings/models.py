from django.db import models
from django_project.base_model import BaseModel, ImgModel


class PaySystem(ImgModel):
    """"""
    name = models.TextField(verbose_name='Платежная система', unique=True, blank=False, default=None)
    img_url = models.ImageField(upload_to='images/shop_settings/pay_system')


class Socical(ImgModel):
    """"""
    name = models.TextField(verbose_name='Название соц.сети')
    description = models.TextField(verbose_name='ссылка на соц.сеть')
    img_url = models.ImageField(upload_to='images/shop_settings/social')


class MarketingBanner(ImgModel):
    """"""
    name = models.TextField(unique=True, blank=False)
    start_date = models.DateTimeField(blank=False, default=None)
    end_date = models.DateTimeField(blank=False, default=None)
    img_url = models.ImageField(upload_to='images/shop_settings/marketing_banner')

    def __str__(self):
        return self.name + " завершение: " + str(self.end_date)

class Settings(BaseModel):
    """"""
    logo = models.ImageField(blank=False, upload_to='images/shop_settings/logo')
    phone_main = models.TextField(max_length=500, blank=False)
    phone_sec = models.TextField(max_length=500, blank=False)
    copyright = models.TextField(max_length=500, blank=False)
    social = models.ManyToManyField(Socical, related_name="socials", blank=False)
    pay_system = models.ManyToManyField(PaySystem, related_name="socials", blank=False)
    marketing_banners = models.ManyToManyField(MarketingBanner, related_name="mk", blank=False)

    def __str__(self):
        return str('main settings model')
