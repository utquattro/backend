from django.db import models
from e_shop.services import translate_text
from django.core.validators import MinValueValidator


class CharacteristicValue(models.Model):
    objects = models.Manager()
    value = models.CharField(max_length=50, verbose_name='Значение')
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.value


class Characteristic(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=30, unique=True, verbose_name='Название')
    values = models.ManyToManyField(CharacteristicValue, verbose_name='Значение')
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    img_url = models.ImageField(blank=True, upload_to='images/goods/brands', verbose_name='Лого бренда' )
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name


class Categorie(models.Model):
    """"""
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    category_name = models.TextField(max_length=250, blank=False, default='1', verbose_name='Категория')
    title = models.TextField(max_length=250, blank=False)
    characteristics = models.ManyToManyField(Characteristic, verbose_name='Фильтр')
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    img_url = models.ImageField(blank=True, upload_to='images/goods/categories',)
    link_url = models.TextField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def save(self, *args, **kwargs):
        self.category_name = f"{translate_text(str(self.title))}"
        self.link_url = f"{self.category_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductSku(models.Model):
    """"""
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    sku = models.TextField(max_length=100, blank=True, null=True, unique=True, verbose_name='Артикул')
    characteristics = models.ManyToManyField(CharacteristicValue, verbose_name='Характеристики')
    price = models.PositiveIntegerField(blank=True,
                                        null=True,
                                        validators=[MinValueValidator(1)],
                                        verbose_name='Цена')
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    img_url = models.ImageField(blank=True, upload_to='images/goods/product', )
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.sku


class Product(models.Model):
    """"""
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, verbose_name='Категория')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, verbose_name='Бренд')
    skus = models.ManyToManyField(ProductSku, verbose_name='Артикулы')
    name = models.TextField(max_length=250, blank=True, default='1')
    title = models.TextField(max_length=250, blank=False)
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    img_url = models.ImageField(blank=True, upload_to='images/goods/product', )
    link_url = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def save(self, *args, **kwargs):
        self.name = f"{translate_text(str(self.title))}"
        self.link_url = f"{self.name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title








