from django.forms import ModelForm
from .models import Booking


# loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
