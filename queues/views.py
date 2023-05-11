from rest_framework import generics
from .models import Queue

class QueueView(generics.ListCreateAPIView):
    queryset = Queue