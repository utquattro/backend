from django.db import models


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


class ImgModel(BaseModel):
    name = models.TextField(max_length=250, blank=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    img_url = models.ImageField(blank=False, upload_to='images/unsort')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

