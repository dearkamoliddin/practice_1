from django.shortcuts import render

from cars.models import CarModel


def home_view(request):
    car = CarModel.objects.all()
    context = {
        'cars_list': car
    }
    return render(request, 'home.html', context)
