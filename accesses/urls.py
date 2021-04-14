from django.urls import path

from .views import DoorUseLogListGV

urlpatterns = [
    path('/access', DoorUseLogListGV.as_view(), name='access-list'),
]