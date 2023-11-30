from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Pin(models.Model):
    profile = models.ForeignKey(
        User, related_name='pins', on_delete=models.PROTECT)
    title = models.CharField(
        'Pin Title', max_length=200, blank=True, null=True)
    description = models.CharField(
        'Pin Description', max_length=300, blank=True, null=True)
    image = models.CharField('Pin Image URL', max_length=500)
    origin = models.CharField('Pin Website', max_length=100)
    path = models.CharField('Pin Path', max_length=100)

    def __str__(self) -> str:
        return f'{self.id} / {self.path}'

    class Meta:
        db_table = 'pins'
        verbose_name_plural = 'Pins'
