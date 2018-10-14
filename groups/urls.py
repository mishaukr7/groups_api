from django.urls import path, include
from .views import *

app_name = 'groups'

urlpatterns = [
    path('groups/', GroupView.as_view(), name='groups'),
    path('groups/<int:pk>', GroupDetailView.as_view(), name='group'),
    path('groups/<int:group>/elements/', ElementListView.as_view(), name='group-elements'),

]
