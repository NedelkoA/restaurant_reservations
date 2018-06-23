from django import forms
from .models import Reservation
from datetime import datetime


class ReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            if kwargs['instance']:
                choices = [
                    (table, 'Table ' + str(table))
                    for table in range(1, kwargs['instance'].number_seats + 1)
                ]
                self.fields['table'] = forms.ChoiceField(choices=choices)

    class Meta:
        model = Reservation
        fields = ['date', 'time', 'visitors', 'table']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'min': str(datetime.date(datetime.today()))
                }
            ),
            'time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'min': '10:00',
                    'max': '20:00'
                }
            )
        }
