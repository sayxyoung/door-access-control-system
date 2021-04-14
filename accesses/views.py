from django.shortcuts import redirect

from rest_framework             import generics
from rest_framework.decorators  import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response    import Response
from rest_framework.views       import APIView
from rest_framework.views       import status

from accounts.models import Generation
from .models         import DoorUseLog
from .permissions    import IsAdminOrGeneration
from .serializers    import DoorUseLogSerializer, GenerationSerializer


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


class GenerationAdminAV(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        generations = Generation.objects.all()
        serializer  = GenerationSerializer(generations, many=True)
        return Response(serializer.data)


class GenerationPublicAV(APIView):
    permission_classes = [IsAdminOrGeneration]

    def get(self, request, generation):
        try:
            generation = Generation.objects.get(name=generation)
            self.check_object_permissions(self.request, generation)
        except Generation.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = GenerationSerializer(generation)
        return Response(serializer.data)

@api_view(['GET'])
def api_list(request):
    if request.method == 'GET':
        api_list = {
            'ApiList'             : 'api/list',
            'DoorUseLogList'      : 'api/access',
            'DoorUseLogListDetail': 'api/access/<str:generation>',
            'GenerationAdmin'     : 'api/admin',
            'GenerationPublic'    : 'api/public/<str:generation>',
        }
        return Response(api_list)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

def index(request):
    return redirect('/api/list')