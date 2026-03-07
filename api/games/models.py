from django.db import models

class Game(models.Model):
    map = models.ForeignKey("maps.Map", on_delete=models.CASCADE, related_name="games")



class Player(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="players")
    number = models.IntegerField()
    funds = models.IntegerField()



class Unit(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="units")
    tile = models.ForeignKey("maps.Tile", on_delete=models.CASCADE, related_name="units")
    type = models.CharField(max_length=2)
    health = models.IntegerField()



class TileOwnership(models.Model):
    owner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="tile_ownerships")
    tile = models.ForeignKey("maps.Tile", on_delete=models.CASCADE, related_name="ownerships")
    is_hq = models.BooleanField(default=False)