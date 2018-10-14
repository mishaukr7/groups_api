from rest_framework import generics
from .serializers import GroupSerializer, ElementSerializer
from .models import Group, Element
from rest_framework.pagination import PageNumberPagination


class GroupView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = PageNumberPagination


class GroupDetailView(generics.RetrieveUpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = PageNumberPagination


class ElementListView(generics.ListCreateAPIView):
    serializer_class = ElementSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        group = self.kwargs['group']
        return Element.objects.filter(group=group)


