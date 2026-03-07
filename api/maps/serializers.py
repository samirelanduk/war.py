from rest_framework import serializers
from .models import Map, Tile

class MapListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ["id", "name", "width", "height"]


class TileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tile
        fields = ["x", "y", "type"]


class MapDetailSerializer(serializers.ModelSerializer):
    tiles = TileSerializer(many=True, read_only=True)

    class Meta:
        model = Map
        fields = ["id", "name", "width", "height", "tiles"]
