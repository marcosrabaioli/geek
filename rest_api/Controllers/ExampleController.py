from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.


class ExampleList(generics.ListAPIView):

    queryset = []
    permission_classes = [AllowAny]