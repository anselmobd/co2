from django.db import models


# Create your models here.
class Subscribers(models.Model):
    email = models.CharField(
        max_length=100, blank=False, null=False, help_text='E-mail')
    full_name = models.CharField(
        max_length=200, blank=False, null=False, help_text='Nome completo')

    def __str__(self):
        """String representation of subscribers"""
        return self.full_name

    class Meta:
        verbose_name = "Pesssoa"
