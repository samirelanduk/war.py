from django.core.management.base import BaseCommand
from maps.models import Map

class Command(BaseCommand):
    help = "Create a map from a text file"

    def add_arguments(self, parser):
        parser.add_argument("name", help="Name for the map")
        parser.add_argument("path", help="Path to the map text file")

    def handle(self, *args, **options):
        map_obj = Map.from_file(options["name"], options["path"])
        self.stdout.write(
            self.style.SUCCESS(f"Created map '{map_obj.name}' ({map_obj.width}x{map_obj.height})")
        )
