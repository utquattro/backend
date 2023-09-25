from django.db import models


class Phone(models.Model):
    """"""

    class Position(models.IntegerChoices):
        FIRST = 1
        SECOND = 2

    objects = models.Manager()
    number = models.TextField(max_length=50, blank=False)
    position = models.IntegerField(choices=Position.choices, unique=True, null=True)
    description = models.TextField(max_length=500, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.number


class Socical(models.Model):
    """"""
    objects = models.Manager()
    name = models.TextField(max_length=50, blank=False)
    description = models.TextField(max_length=500, blank=True)
    link = models.TextField(max_length=500, blank=False)
    img_url = models.ImageField(blank=False, upload_to='images/shop_settings/social', )
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name


class Copyright(models.Model):
    """"""
    objects = models.Manager()
    name = models.TextField(max_length=50, blank=False)
    description = models.TextField(max_length=500, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name


class PaySystem(models.Model):
    """"""
    objects = models.Manager()
    pay_system_name = models.TextField(max_length=50, blank=False)
    description = models.TextField(max_length=500, blank=True)
    img_url = models.ImageField(blank=False, upload_to='images/shop_settings/pay_system', )
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.pay_system_name


class Logo(models.Model):
    """"""
    objects = models.Manager()
    title = models.TextField(max_length=250, blank=False)
    description = models.TextField(max_length=500, blank=True)
    logo_url = models.ImageField(blank=False, upload_to='images/shop_settings/logo', )
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(blank=True)

    def __str__(self):
        return self.title

