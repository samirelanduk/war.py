from django.db import models

class Map(models.Model):
    name = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return self.name



class TileType(models.TextChoices):
    GRASS    = "G", "Grass"
    SEA      = "S", "Sea"
    FOREST   = "F", "Forest"
    MOUNTAIN = "M", "Mountain"
    RIVER    = "V", "River"
    ROAD     = "R", "Road"
    BRIDGE   = "B", "Bridge"



class Tile(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.IntegerField()
    type = models.CharField(max_length=1, choices=TileType.choices)