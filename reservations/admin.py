from django.contrib import admin
from .models import Restaurant, Table, TimeSlot, Reservation


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone']
    search_fields = ['name', 'address']


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['number', 'capacity', 'is_available']
    list_filter = ['is_available', 'capacity']
    search_fields = ['number']


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['start_time', 'end_time', 'is_available']
    list_filter = ['is_available']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'table', 'date', 'time_slot', 'status', 'created_at']
    list_filter = ['date', 'status', 'table']
    search_fields = ['user__username', 'table__number']
    actions = ['confirm_reservation', 'cancel_reservation']

    def confirm_reservation(self, request, queryset):
        queryset.update(status='confirmed')
        self.message_user(request, "Выбранные бронирования были подтверждены")

    confirm_reservation.short_description = "Подтвердить выбранные бронирования"

    def cancel_reservation(self, request, queryset):
        queryset.update(status='cancelled')
        self.message_user(request, "Выбранные бронирования были отменены")

    cancel_reservation.short_description = "Отменить выбранные бронирования"
