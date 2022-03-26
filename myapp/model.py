from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models

class AlcoholicProduct(models.Model):

    name = models.CharField(
        verbose_name='NAME',
        max_length=16,
        validators=[MaxLengthValidator(16)]
    )
    product_type = models.CharField(
        verbose_name='PRODUCT_TYPE',
        max_length=16,
        validators=[MaxLengthValidator(16)
                    ]
    )
    manufacturer = models.CharField(
        verbose_name='MANUFACTURER',
        max_length=16,
        validators=[MaxLengthValidator(16)]
    )
    degree = models.DecimalField(
        verbose_name='DEGREE',
        max_digits=4,
        decimal_places=1,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(100.0)
        ]
    )
    price = models.IntegerField(
        verbose_name='PRICE',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10000)
        ]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'product_type', 'manufacturer'],
                name='unique_keys'
            ),
        ]
