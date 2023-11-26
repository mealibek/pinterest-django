from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Pin(models.Model):
    profile = models.ForeignKey(
        User, related_name='pins', on_delete=models.PROTECT)
    title = models.CharField('Pin Title', max_length=200)
    description = models.CharField('Pin Description', max_length=300)
    image = models.CharField('Pin Image URL', max_length=500)
    website = models.CharField('Pin Website', max_length=100)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'pins'
        verbose_name_plural = 'Pins'
