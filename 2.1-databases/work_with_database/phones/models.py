from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50, default=None)
    release_date = models.DateField(verbose_name='Release Date', default=None)
    price = models.FloatField(verbose_name='Price', default=0)
    image = models.URLField(verbose_name='IMG URL', default=None)
    lte_exists = models.BooleanField(verbose_name='LTE', default=0)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL", default=None)

    def __str__(self):
        return f'{self.name}, {self.price}'

    def get_absolute_url(self):
        return reverse("phone", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)