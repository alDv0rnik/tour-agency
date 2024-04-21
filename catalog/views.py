from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from catalog.models import Country, Tour


def index(request):
    countries = Country.objects.all()
    return render(request, "base.html", context={
        "countries": countries,
        "title": "Tour Agency - Главная страница"
    })


def get_tours(request):
    if request.method == "POST":
        duration_ = request.POST.get("duration")
        is_family = request.POST.get("is_family")
        country = request.POST.get("countries")
        if country and duration_ and is_family:
            tours = Tour.objects.filter(destination__name=country, duration=int(duration_), is_family=is_family)

        return render(
            request,
            "tours.html",
            context={
                "title": "Tour Agency - Список туров",
                "tours": tours
            })
    return redirect("home")

