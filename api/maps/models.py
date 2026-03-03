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