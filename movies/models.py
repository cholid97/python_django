from django.db import models


class Mpaarating(models.Model):
    type = models.CharField(max_length=100)
    label = models.TextField()


class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    img_path = models.TextField()
    duration = models.IntegerField()  # in minutes
    genres = models.TextField()
    language = models.CharField(max_length=50)
    mpaa_rating_id = models.ForeignKey(Mpaarating, on_delete=models.CASCADE, null=True)
    user_rating = models.IntegerField()
