from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from django_project.services import translate_text


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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, blank=True, help_text='If this object is active')
    objects = models.Manager()
    active_objects = ActiveManager()
    inactive_objects = InactiveManager()

    class Meta:
        abstract = True


class Brand(BaseModel):
    """
        Бренд товаров
    """
    name = models.CharField(max_length=50, unique=True, verbose_name='Название бренда')
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name='Описание бренда')
    img_url = models.ImageField(blank=True, upload_to='images/goods/brands',
                                verbose_name='Лого бренда')

    def __str__(self):
        return self.name


class Categorie(BaseModel):
    """
        Категории товаров
    """
    name = models.TextField(max_length=250, blank=False,
                            verbose_name='Название категории')
    img_url = models.ImageField(blank=True, upload_to='images/goods/categories', )
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Product(BaseModel):
    """"""
    name = models.TextField(max_length=250, blank=False, verbose_name='Название продукта')
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, verbose_name='Категория')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, verbose_name='Бренд продукта')
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name='Описание товара')
    img_url = models.ImageField(blank=True, upload_to='images/goods/product', )
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})


class CharacteristicName(BaseModel):
    name = models.CharField(max_length=50, unique=True, blank=False,
                            verbose_name='Имя характеристики')

    def __str__(self):
        return self.name


class CharacteristicValue(BaseModel):
    value = models.CharField(max_length=50, unique=True, blank=False,
                             verbose_name='Значение характеристики')

    def __str__(self):
        return self.value


class Characteristic(BaseModel):
    name = models.ForeignKey(CharacteristicName, on_delete=models.CASCADE, blank=False, default=None,
                             verbose_name='Значение характеристики')
    value = models.ForeignKey(CharacteristicValue, on_delete=models.CASCADE, blank=False, default=None,
                              verbose_name='Значение характеристики')

    def __str__(self):
        return str(self.name) + " " + str(self.value)

    class Meta:
        unique_together = ('name', 'value')


class ProductSku(BaseModel):
    """"""
    sku = models.TextField(max_length=100, blank=True, null=True, unique=True,
                           verbose_name='Артикул товара')
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE, default=None)
    characteristics = models.ManyToManyField(Characteristic, related_name="sku_char")
    price = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1)],
                                        verbose_name='Цена')
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name='Описание артикула товара')
    img_url = models.ImageField(blank=True, upload_to='images/goods/product', )

    def __str__(self):
        return self.sku
