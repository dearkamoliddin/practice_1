from django.urls import path

from cars.views import home_view


urlpatterns = [
    path('', home_view)
]
