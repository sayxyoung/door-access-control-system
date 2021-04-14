from rest_framework             import generics
from rest_framework.permissions import IsAdminUser

from .models         import DoorUseLog
from .serializers    import DoorUseLogSerializer


class DoorUseLogListGV(generics.ListAPIView):
    queryset           = DoorUseLog.objects.all()
    serializer_class   = DoorUseLogSerializer
    permission_classes = [IsAdminUser]