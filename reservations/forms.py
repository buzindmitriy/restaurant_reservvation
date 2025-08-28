from django import forms
from .models import Reservation, Table, TimeSlot
from datetime import date


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'date', 'time_slot']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')}),
            'table': forms.Select(attrs={'class': 'form-control'}),
            'time_slot': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Фильтруем доступные столики и временные слоты
        self.fields['table'].queryset = Table.objects.filter(is_available=True)
        self.fields['time_slot'].queryset = TimeSlot.objects.filter(is_available=True)

        # Устанавливаем минимальную дату
        today = date.today()
        self.fields['date'].widget.attrs.update({'min': today.strftime('%Y-%m-%d')})
