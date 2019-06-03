from django.conf import settings
from django.db import models

__all__ = ("University",)


class University(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=512, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Universities"

    def __str__(self):
        return "%s_%s" % (self.name, self.owner)

    def __repr__(self):
        return "%s_%s" % (self.name, self.owner)
