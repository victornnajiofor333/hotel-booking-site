from datetime import date
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest_name', 'email', 'phone', 'check_in', 'check_out']
        widgets = {
            'guest_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'check_in': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, room=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.room = room

    def clean(self):
        cleaned = super().clean()
        check_in = cleaned.get('check_in')
        check_out = cleaned.get('check_out')

        if check_in and check_out:
            if check_in < date.today():
                raise forms.ValidationError("Check-in date cannot be in the past.")
            if check_out <= check_in:
                raise forms.ValidationError("Check-out must be after check-in.")
            if self.room:
                clash = Booking.objects.filter(
                    room=self.room,
                    check_in__lt=check_out,
                    check_out__gt=check_in,
                ).exists()
                if clash:
                    raise forms.ValidationError(
                        "This room is already booked for those dates. Please choose different dates."
                    )
        return cleaned