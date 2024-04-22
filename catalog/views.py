from django.shortcuts import render, redirect
from django.views.generic import ListView

from catalog.models import Country, Tour


def index(request):
    countries = Country.objects.all()
    return render(request, "index.html", context={
        "countries": countries,
        "title": "Tour Agency - Главная страница"
    })


class TourListView(ListView):
    model = Tour
    template_name = "tours.html"
    context_object_name = "tours"

    def get_context_data(self, **kwargs):
        context = super(TourListView, self).get_context_data(**kwargs)
        context["title"] = "Tour Agency - Список туров"
        return context


def get_tours(request):
    if request.method == "POST":
        duration = request.POST.get("duration")
        is_family = request.POST.get("is_family", False)
        country = request.POST.get("countries")
        if country and duration:
            tours = Tour.objects.filter(destination__name=country, duration=int(duration), is_family=bool(is_family))
        elif country and not duration:
            tours = Tour.objects.filter(destination__name=country, is_family=bool(is_family))
        elif duration and not country:
            tours = Tour.objects.filter(duration=int(duration), is_family=bool(is_family))
        else:
            return redirect("home")

        return render(
            request,
            "tours.html",
            context={
                "title": "Tour Agency - Список туров",
                "tours": tours
            })


