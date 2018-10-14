from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from .managers import ElementsManager
# Create your models here.


class Group(MPTTModel):
    name = models.CharField(max_length=64, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,
                            on_delete=models.CASCADE)
    description = models.TextField(blank=True, default='', max_length=512)
    icon = models.ImageField(upload_to='icons/groups/')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'groups'

    def __str__(self):

        full_path = [self.name]
        k = self.parent

        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return '/'.join(full_path[::-1])

    @property
    def children_groups_count(self):
        return self.get_descendant_count

    @property
    def children_elements_count(self):
        elements = self.get_descendants(include_self=True)
        return elements.count()


class Element(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, default='', max_length=512)
    icon = models.ImageField(upload_to='icons/groups/')
    group = TreeForeignKey('Group', on_delete=models.CASCADE, related_name='element_child')
    created = models.DateTimeField(auto_now_add=True)
    is_checked = models.NullBooleanField()
    objects = ElementsManager()
    manager = models.Manager()

    class Admin:
        manager = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'elements'

