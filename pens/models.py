from django.db import models

from brands.models import Brand
from pens.enum import NibMaterial, NibSize


class Pen(models.Model):
    name = models.CharField(max_length=255)
    nib_size = models.CharField(max_length=10)
    nib_material = models.CharField(max_length=100)
    description = models.TextField(null=True)
    colour = models.CharField(max_length=100)
    purchase_price = models.FloatField()
    purchase_currency = models.CharField(max_length=3)
    retailer = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    purchased_date = models.DateField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    class Meta:
        indexes = [models.Index(fields=["nib_size", "colour", "purchase_currency"])]

    @property
    def nib_material_full(self):
        return NibMaterial[self.nib_material].value

    @property
    def nib_size_full(self):
        return NibSize[self.nib_size].value

    @property
    def full_name(self):
        return f"{self.brand.name} {self.name}"
