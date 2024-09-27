from django.db import models


class ZipModel(models.Model):
    cold = models.IntegerField(null=True)
    warm = models.IntegerField(null=True)
    electric = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Зиповская'
        verbose_name_plural = 'Зиповская'


class ShkolnaiaModel(models.Model):
    cold_kitchen = models.IntegerField(null=True)
    warm_kitchen = models.IntegerField(null=True)
    cold_bath = models.IntegerField(null=True)
    warm_bath = models.IntegerField(null=True)
    electric = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Школьная'
        verbose_name_plural = 'Школьная'
