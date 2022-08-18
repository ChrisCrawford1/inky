from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)
    country_of_origin = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [models.Index(fields=["name"])]
