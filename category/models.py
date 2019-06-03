from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from university.models import (
    University
)

__all__ = ("Category",)


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_final = models.BooleanField(default=False)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
