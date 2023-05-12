from django_filters import rest_framework as filters
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


class QueueFilter(filters.FilterSet):
    section_code = filters.CharFilter(
        field_name="section_code", lookup_expr="icontains"
    )
    section_name = filters.CharFilter(
        field_name="section_name", lookup_expr="icontains"
    )
    division_code = filters.CharFilter(
        field_name="division_code", lookup_expr="icontains"
    )
    division_name = filters.CharFilter(
        field_name="division_name", lookup_expr="icontains"
    )
    class_code = filters.CharFilter(field_name="class_code", lookup_expr="icontains")
    class_name = filters.CharFilter(field_name="class_name", lookup_expr="icontains")

    class Meta:
        model = Queue
        fields = [
            "section_code",
            "section_name",
            "division_code",
            "division_name",
            "class_code",
            "class_name",
        ]


class QueueFilterView(generics.ListAPIView):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer

    lookup_url_kwarg = [
        "section_code",
        "section_name",
        "division_code",
        "division_name",
        "class_code",
        "class_name",
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = QueueFilter
