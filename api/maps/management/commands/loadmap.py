from django.core.management.base import BaseCommand
from maps.models import Map


class Command(BaseCommand):
    help = "Create a map from a JSON file"

    def add_arguments(self, parser):
        parser.add_argument("name", help="Name for the map")
        parser.add_argument("path", help="Path to the map JSON file")
        parser.add_argument("--update", action="store_true", help="Replace tiles/units if map already exists")

    def handle(self, *args, **options):
        try:
            map_obj = Map.from_file(options["name"], options["path"], update=options["update"])
        except ValueError as e:
            self.stderr.write(self.style.ERROR(str(e)))
            return
        verb = "Updated" if options["update"] else "Created"
        self.stdout.write(
            self.style.SUCCESS(f"{verb} map '{map_obj.name}' ({map_obj.width}x{map_obj.height})")
        )
