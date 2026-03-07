from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Map
from .serializers import MapListSerializer, MapDetailSerializer

class MapListView(ListAPIView):
    queryset = Map.objects.all()
    serializer_class = MapListSerializer


class MapDetailView(RetrieveAPIView):
    queryset = Map.objects.prefetch_related("tiles")
    serializer_class = MapDetailSerializer
