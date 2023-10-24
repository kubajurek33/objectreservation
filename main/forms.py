from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    day = forms.DateField(label="dzien")
    time = forms.CharField(label="czas")
    class Meta:
        model = Reservation
        fields = ('day', 'time')
