from django.db import models
from e_shop.services import translate_text
from django.core.validators import MinValueValidator


# Create your models here.
class Categorie(models.Model):
    """"""
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    category_name = models.TextField(max_length=250, blank=False, default='1')
    title = models.TextField(max_length=250, blank=False)
    description = models.TextField(max_length=500, blank=True)
    img_url = models.ImageField(blank=True, upload_to='images/goods/categories', )
    link_url = models.TextField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def save(self, *args, **kwargs):
        self.category_name = f"{translate_text(str(self.title))}"
        self.link_url = f"{self.category_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(models.Model):
    """"""
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    name = models.TextField(max_length=250, blank=True, default='1')
    title = models.TextField(max_length=250, blank=False)
    description = models.TextField(max_length=500, blank=True)
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


class PropertyName(models.Model):
    """"""
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=500, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name




class PropertyValue(models.Model):
    """"""
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    value = models.TextField(max_length=500, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.value


class Property(models.Model):
    """"""
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    property_name = models.ForeignKey(PropertyName, on_delete=models.CASCADE, null=True)
    property_value = models.ForeignKey(PropertyValue, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return str(self.id) + " " + str(self.property_name) + " " + str(self.property_value)

    class Meta:
        unique_together = ('property_name', 'property_value')


class ProductSku(models.Model):
    """"""
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku = models.TextField(max_length=100, blank=True, null=True, unique=True)
    price = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1)])
    description = models.TextField(max_length=500, blank=True)
    img_url = models.ImageField(blank=True, upload_to='images/goods/product', )
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.sku


class ProductConfig(models.Model):
    """"""
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    product_property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True)
    product_item = models.ForeignKey(ProductSku, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    class Meta:
        unique_together = ('product_property', 'product_item')


class CategoryPropertyConfig(models.Model):
    """"""
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    product_property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    class Meta:
        unique_together = ('product_property', 'category')

