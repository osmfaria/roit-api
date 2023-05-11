from rest_framework import generics
from .models import Queue
from .serializers import QueueSerializer

class QueueView(generics.ListCreateAPIView):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer 