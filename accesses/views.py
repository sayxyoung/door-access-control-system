from rest_framework             import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response    import Response
from rest_framework.views       import APIView
from rest_framework.views       import status

from .models         import DoorUseLog
from .permissions    import IsAdminOrGeneration
from .serializers    import DoorUseLogSerializer


class DoorUseLogListGV(generics.ListAPIView):
    queryset           = DoorUseLog.objects.all()
    serializer_class   = DoorUseLogSerializer
    permission_classes = [IsAdminUser]


class DoorUseLogDetailListAV(APIView):
    permission_classes = [IsAdminOrGeneration]

    def get(self, request, generation):
        dooruselogs = DoorUseLog.objects.filter(generation__name=generation)
        if not dooruselogs:
            return Response(status=status.HTTP_204_NO_CONTENT)
        self.check_object_permissions(self.request, dooruselogs[0])
        serializer = DoorUseLogSerializer(dooruselogs, many=True)
        return Response(serializer.data)