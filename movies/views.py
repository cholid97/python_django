from django.core import serializers
from django.db.models import Aggregate, F, Func, OuterRef, Q, Subquery, Value
from django.db.models.functions import Coalesce
from django.http import HttpResponse
from django.shortcuts import render

from .models import Movie, Mpaarating


def index(request):
    return HttpResponse("Hello GUYS Firs Try")


def list(request):
    query = request.GET.get("q")
    if query or query == "":
        movies = Movie.objects.filter(Q(name__icontains=query)).all()

        data = serializers.serialize("json", movies)
        return HttpResponse(data, content_type="application/json")
    else:
        movies = Movie.objects.all()
    return render(request, "list.html", {"movies": movies})


def detail(request, movie_id):

    movie = Movie.objects.select_related("mpaa_rating_id").get(id=movie_id)
    return render(request, "details.html", {"movie": movie})
