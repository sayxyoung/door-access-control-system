from django.urls import path

from .views import (
    DoorUseLogListGV, DoorUseLogDetailListAV,
)

urlpatterns = [
    path('/access', DoorUseLogListGV.as_view(), name='access-list'),
    path('/access/<str:generation>', DoorUseLogDetailListAV.as_view(), name='access-detail'),
]