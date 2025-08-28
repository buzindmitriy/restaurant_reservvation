from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Reservation, Table, TimeSlot
from .forms import ReservationForm
from datetime import date


def home(request):
    """Главная страница"""
    return render(request, 'reservations/index.html')


@login_required
def make_reservation(request):
    """Форма бронирования"""
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, 'Бронирование успешно создано!')
            return redirect('reservation_list')
    else:
        form = ReservationForm()

    return render(request, 'reservations/reservation_form.html', {'form': form})


@login_required
def reservation_list(request):
    """Список бронирований пользователя"""
    reservations = Reservation.objects.filter(user=request.user).order_by('-date')
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})


def get_available_tables(request):
    """Получение доступных столиков для выбранной даты и времени"""
    date_str = request.GET.get('date')
    time_id = request.GET.get('time_slot')

    # Фильтрация доступных столиков
    available_tables = Table.objects.filter(is_available=True)

    # Здесь можно добавить логику проверки занятости столиков
    # Например, проверка пересечений с другими бронированиями

    tables_data = [{'id': table.id, 'number': table.number, 'capacity': table.capacity}
                   for table in available_tables]

    return JsonResponse({'tables': tables_data})