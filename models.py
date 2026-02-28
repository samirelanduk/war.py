from __future__ import annotations
from enum import Enum
from dataclasses import dataclass

@dataclass
class Game:
    map: Map

@dataclass
class Player:
    game: Game

@dataclass
class Unit:
    x: int
    y: int
    player: Player
    game: Game



@dataclass
class Map:
    width: int
    height: int

@dataclass
class Tile:
    x: int
    y: int
    map: Map
    type: TileType


class TileType(Enum):
    GRASS = "grass"
    ROAD = "road"
    RIVER = "river"
    SEA = "sea"
    MOUNTAIN = "mountain"
    FOREST = "forest"


