from django.db import models

class Map(models.Model):
    name = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return self.name

    @staticmethod
    def from_file(name, path):
        with open(path) as f: lines = f.read().strip().splitlines()
        map_obj = Map.objects.create(name=name, width=len(lines[0]), height=len(lines))
        Tile.objects.bulk_create([
            Tile(map=map_obj, x=x, y=y, type=char)
            for y, line in enumerate(lines)
            for x, char in enumerate(line)
        ])
        return map_obj



class TileType(models.TextChoices):
    GRASS    = "GR", "Grass"
    SEA      = "SE", "Sea"
    BEACH    = "BE", "Beach"
    FOREST   = "FR", "Forest"
    MOUNTAIN = "MT", "Mountain"
    RIVER    = "RV", "River"
    ROAD     = "RO", "Road"
    BRIDGE   = "BR", "Bridge"
    CITY     = "CT", "City"
    FACTORY  = "FC", "Factory"
    PORT     = "PO", "Port"
    AIRPORT  = "AP", "Airport"
    HQ       = "HQ", "Headquarters"



class Tile(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name="tiles")
    x = models.IntegerField()
    y = models.IntegerField()
    initial_owner = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=2, choices=TileType.choices)



class Game(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name="games")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name