from django.db import models

# Create your models here.


class McFoodInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    calories = models.CharField(max_length=100, verbose_name='Calories')
    fats = models.CharField(max_length=100, verbose_name='Fats')
    carbs = models.CharField(max_length=100, verbose_name='Carbs')
    proteins = models.CharField(max_length=100, verbose_name='Proteins')
    unsaturated_fats = models.CharField(max_length=100, verbose_name='Unsaturated Fats')
    sugar = models.CharField(max_length=100, verbose_name='Sugar')
    salt = models.CharField(max_length=100, verbose_name='Salt')
    portion = models.CharField(max_length=100, verbose_name='Portion')

    class Meta:
        pass

    def __str__(self):
        return self.name
