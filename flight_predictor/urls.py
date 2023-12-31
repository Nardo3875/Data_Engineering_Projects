from django.urls import path
from flights.views import index, predict_flight_price

urlpatterns = [
    path('', index, name='index'),
    path('predict/', predict_flight_price, name='predict_flight_price'),
]
