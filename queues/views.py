from rest_framework import generics
from rest_framework.views import Response, status

from .models import Queue
from .serializers import QueueSerializer

class QueueView(generics.ListCreateAPIView):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer

class QueueDeleteView(generics.DestroyAPIView):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer

    def destroy(self, request, *args, **kwargs):
        self.queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)