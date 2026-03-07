import json

from django.db import models, transaction


class Map(models.Model):
    name = models.CharField(max_length=255, unique=True)

    @property
    def width(self):
        agg = self.tiles.aggregate(max_x=models.Max("x"))
        return (agg["max_x"] or 0) + 1

    @property
    def height(self):
        agg = self.tiles.aggregate(max_y=models.Max("y"))
        return (agg["max_y"] or 0) + 1

    @staticmethod
    def from_file(name, path, *, update=False):
        with open(path) as f:
            data = json.load(f)
        with transaction.atomic():
            existing = Map.objects.filter(name=name).first()
            if existing and not update:
                raise ValueError(f"Map '{name}' already exists")
            if existing and update:
                existing.tiles.all().delete()
                map_obj = existing
            else:
                map_obj = Map.objects.create(name=name)
            tile_lookup = {}
            for td in data["tiles"]:
                tile = Tile.objects.create(
                    map=map_obj,
                    x=td["x"],
                    y=td["y"],
                    type=td["type"],
                    owner=td.get("owner"),
                    is_hq=td.get("is_hq", False),
                )
                tile_lookup[(td["x"], td["y"])] = tile
            for ud in data.get("units", []):
                tile = tile_lookup[(ud["x"], ud["y"])]
                MapUnit.objects.create(
                    map=map_obj,
                    tile=tile,
                    owner=ud["owner"],
                    type=ud["type"],
                )
        return map_obj


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