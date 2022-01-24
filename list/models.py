from django.db import models


# Create your models here.
class DataTODO(models.Model):
    data_todo = models.TextField(verbose_name='Задача')
    style_todo = models.CharField(max_length=200, verbose_name='Стиль', null=True, default='-')

    def __str__(self):
        return self.data_todo

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
