from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Table(models.Model):
    number = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Столик {self.number} ({self.capacity} мест)"


class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Ожидает подтверждения'),
            ('confirmed', 'Подтверждено'),
            ('cancelled', 'Отменено'),
        ],
        default='pending'
    )

    def __str__(self):
        return f"Бронь {self.user.username} на {self.date} {self.time_slot}"

