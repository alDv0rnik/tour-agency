from django.shortcuts import render

from catalog.models import Tour
from orders.models import Order, OrderInfo
from .forms import OrderInfoEditForm, DateEditForm


def create_order(request, tour_slug):
    tour = Tour.objects.get(slug=tour_slug)
    if request.method == 'POST':
        form = OrderInfoEditForm(request.POST)
        date_form = DateEditForm(request.POST)
        if form.is_valid() and date_form.is_valid():
            order = Order.objects.create()
            order.tour.add(tour)
            OrderInfo.objects.create(
                order=order,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                city=form.cleaned_data['city'],
                members=form.cleaned_data['members']
            )
            return render(request, "created.html", {"order": order})
    else:
        form = OrderInfoEditForm()
        date_form = DateEditForm()
    return render(request, "create.html",
    context={
        "form": form,
        "date_form": date_form,
        "tour": tour
    })