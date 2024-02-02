from django.db import models

# Create your models here.
from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title
