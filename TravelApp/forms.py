from django import forms


from TravelApp.models import Shipment

class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['fullname', 'email', 'phone', 'origin','destination', 'date','message']