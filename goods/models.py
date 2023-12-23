from django.db import models
from django_project.base_model import BaseModel, ImgModel
from django.urls import reverse
from django.core.validators import MinValueValidator


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

    class Meta:
        ordering = ['id']


class CharacteristicName(BaseModel):
    name = models.CharField(max_length=50, unique=True, blank=False,
                            verbose_name='Имя характеристики')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class CharacteristicValue(BaseModel):
    value = models.CharField(max_length=50, unique=True, blank=False,
                             verbose_name='Значение характеристики')

    def __str__(self):
        return self.value

    class Meta:
        ordering = ['value']


class Characteristic(BaseModel):
    name = models.ForeignKey(CharacteristicName, on_delete=models.CASCADE, blank=False, default=None,
                             verbose_name='Имя характеристики')
    value = models.ForeignKey(CharacteristicValue, on_delete=models.CASCADE, blank=False, default=None,
                              verbose_name='Значение характеристики')

    def __str__(self):
        return str(self.name) + " " + str(self.value)

    def get_char_value(self):
        return f"{self.value}"


    class Meta:
        unique_together = ('name', 'value')
        ordering = ['name']


class ProductSku(BaseModel):
    """"""
    name = models.TextField(max_length=250, null=True, verbose_name='Название продукта')
    title = models.TextField(max_length=500, blank=True, null=True, verbose_name='title продукта')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, verbose_name='Бренд продукта')
    category = models.ForeignKey(Categorie, null=True, on_delete=models.CASCADE, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, null=True, db_index=True, verbose_name="URL")
    sku = models.TextField(max_length=100, blank=False, null=True, unique=True,
                           verbose_name='Артикул товара')
    characteristics = models.ManyToManyField(Characteristic, related_name="sku_char")
    price = models.PositiveIntegerField(blank=False, null=True, validators=[MinValueValidator(1)],
                                        verbose_name='Цена')
    stock = models.PositiveIntegerField(blank=False, null=True, validators=[MinValueValidator(0)],
                                        verbose_name='Остаток')
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name='Описание артикула товара')

    img_url = models.ImageField(blank=True, upload_to='images/goods/product', )

    def __str__(self):
        return self.sku

    def save(self, *args, **kwargs):
        self.title = f"{self.brand} {self.name}"
        for i in self.characteristics.all():
           self.title = f"{self.title} {i.get_char_value()}"

        print(self.title)
        super(ProductSku, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['sku']



