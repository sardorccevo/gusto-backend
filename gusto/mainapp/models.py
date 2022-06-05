from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    image = models.CharField(max_length=255, verbose_name='фото')
    price = models.PositiveIntegerField(verbose_name='цена')
    description = models.TextField(verbose_name='описание')
    calories = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='калории')

    TYPE_OF_DISH_CHOICES = [
        ('FS', 'Первое'),
        ('SC', 'Второе'),
        ('DR', 'Питье'),
    ]
    type = models.CharField(
        max_length=2,
        choices=TYPE_OF_DISH_CHOICES,
        default=TYPE_OF_DISH_CHOICES[0],
        verbose_name='тип еды'
    )
    def __str__(self):
        return self.name
