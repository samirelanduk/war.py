from django.db import models

class Map(models.Model):
    name = models.CharField(max_length=255)



class Tile(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name="tiles")
    x = models.IntegerField()
    y = models.IntegerField()
    owner = models.IntegerField(null=True, blank=True)
    is_hq = models.BooleanField(default=False)
    type = models.CharField(max_length=2)



class MapUnit(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name="map_units")
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE, related_name="map_units")
    owner = models.IntegerField()
    type = models.CharField(max_length=2)