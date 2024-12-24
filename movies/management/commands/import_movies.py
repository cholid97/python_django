import json

from django.core.management.base import BaseCommand

from movies.models import Movie, Mpaarating


class Command(BaseCommand):
    help = "Import movies from a JSON file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to the JSON file")

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]

        try:
            with open(file_path, "r") as file:
                data = json.load(file)

                for idx1, item in enumerate(data):
                    # Handle MpaaRating
                    mpaa_data = item["mpaaRating"]
                    mpaa_rating, created = Mpaarating.objects.get_or_create(
                        type=mpaa_data["type"], label=mpaa_data["label"]
                    )

                    name = ""
                    for genre_name in item["genre"]:
                        name += genre_name + ","
                    name = name[:-1]

                    movie = Movie.objects.create(
                        name=item["name"],
                        description=item["description"],
                        img_path=item["imgPath"],
                        duration=item["duration"],
                        language=item["language"],
                        user_rating=item["userRating"],
                        mpaa_rating_id=mpaa_rating,
                        genres=name,
                    )

        except FileNotFoundError:
            self.stderr.write(
                self.style.ERROR("File not found. Please provide a valid file path.")
            )
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {e}"))
