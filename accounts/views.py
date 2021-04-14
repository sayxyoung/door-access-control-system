from rest_framework import generics

from .serializers import UserSerializer


class CreateUserGenericView(generics.CreateAPIView):
    serializer_class = UserSerializer