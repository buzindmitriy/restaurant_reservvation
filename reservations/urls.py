from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reserve/', views.make_reservation, name='make_reservation'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('api/available-tables/', views.get_available_tables, name='available_tables'),
]