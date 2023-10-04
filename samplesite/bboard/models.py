from django.db import models

# Create your models here.

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар') # Title
    content = models.TextField(null=True, blank=True,
                               verbose_name='Описание') # Content
    price = models.FloatField(null=True, blank=True, verbose_name='Цена') # Price
    publised = models.DateTimeField(auto_now_add=True, db_index=True,
                                    verbose_name='Опубликовано') # Date Published


class Meta:
    verbose_name_plural = 'Объяснения'
    verbose_name = 'Объяснение'
    ordering = ['-publised']
