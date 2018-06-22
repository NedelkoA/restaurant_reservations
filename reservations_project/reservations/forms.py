from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time', 'visitors']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
            'time': forms.TimeInput(
                attrs={
                    'type': 'time'
                }
            )
        }
