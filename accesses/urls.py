from django.urls import path

from .views import (
    api_list, index,
    DoorUseLogListGV, DoorUseLogDetailListAV,
    GenerationAdminAV, GenerationPublicAV,
)

urlpatterns = [
    path('', index, name='index'),
    path('/list', api_list, name='api-list'),
    path('/access', DoorUseLogListGV.as_view(), name='access-list'),
    path('/access/<str:generation>', DoorUseLogDetailListAV.as_view(), name='access-detail'),
    path('/admin', GenerationAdminAV.as_view(), name='admin-cost-list'),
    path('/public/<str:generation>', GenerationPublicAV.as_view(), name='public-cost-list'),
]