from django.db import models


class ElementsManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_checked=True)