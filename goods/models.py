from django.db import models
from e_shop.services import translate_text
from django.core.validators import MinValueValidator


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class InactiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=False)


class BaseModel(models.Model):
    """
    Used in all the models as base
    """
    description = models.CharField(max_length=500, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True,
                                 blank=True,
                                 help_text='If this object is active')
    active_objects = ActiveManager()
    inactive_objects = InactiveManager()
    objects = models.Manager()

    class Meta:
        abstract = True


class CharacteristicValue(BaseModel):
    value = models.CharField(max_length=50, verbose_name='Значение')

    def __str__(self):
        return self.value


class Characteristic(BaseModel):
    name = models.CharField(max_length=30, unique=True, verbose_name='Название')
    values = models.ManyToManyField(CharacteristicValue, verbose_name='Значение')

    def __str__(self):
        return self.name


class Brand(BaseModel):
    name = models.CharField(max_length=50, verbose_name='Название')
    img_url = models.ImageField(blank=True, upload_to='images/goods/brands', verbose_name='Лого бренда')

    def __str__(self):
        return self.name


class Categorie(BaseModel):
    """"""

    name = models.TextField(max_length=250, blank=False, verbose_name='Название')
    characteristics = models.ManyToManyField(Characteristic, verbose_name='Фильтр')
    img_url = models.ImageField(blank=True, upload_to='images/goods/categories', )
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    def __str__(self):
        return self.name


class ProductSku(BaseModel):
    """"""
    sku = models.TextField(max_length=100, blank=True, null=True, unique=True, verbose_name='Артикул')

    characteristics = models.ManyToManyField(CharacteristicValue, verbose_name='Характеристики')
    price = models.PositiveIntegerField(blank=True,
                                        null=True,
                                        validators=[MinValueValidator(1)],
                                        verbose_name='Цена')
    img_url = models.ImageField(blank=True, upload_to='images/goods/product', )

    def __str__(self):
        return self.sku


class Product(BaseModel):
    """"""
    name = models.TextField(max_length=250, blank=False, verbose_name='Название')
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, verbose_name='Категория')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, verbose_name='Бренд')
    skus = models.ManyToManyField(ProductSku, verbose_name='Артикулы')
    img_url = models.ImageField(blank=True, upload_to='images/goods/product', )
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    def __str__(self):
        return self.name
