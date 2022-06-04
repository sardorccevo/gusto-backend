from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    image = models.CharField(max_length=255, verbose_name='фото')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='цена')
    description = models.TextField(verbose_name='описание')
    calories = models.PositiveIntegerField(verbose_name='калории')

    def __str__(self):
        return self.name
