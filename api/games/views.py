from rest_framework.generics import ListAPIView, RetrieveAPIView
from games.models import Map
from games.serializers import MapListSerializer, MapDetailSerializer

class MapListView(ListAPIView):
    queryset = Map.objects.all()
    serializer_class = MapListSerializer


class MapDetailView(RetrieveAPIView):
    queryset = Map.objects.prefetch_related("tiles")
    serializer_class = MapDetailSerializer
