from django.contrib import admin
from .models import Element, Group
from mptt.admin import MPTTModelAdmin


class ElementAdmin(admin.ModelAdmin):
    model = Element

    def get_queryset(self, request):
        return self.model.manager.all()


admin.site.register(Element, ElementAdmin)
admin.site.register(Group, MPTTModelAdmin)
