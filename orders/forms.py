from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'first-name'}),
'last_name' : forms.TextInput(attrs={'class':'last-name'}), 'email' : forms.EmailInput(attrs={'class':'email'}), 'address' : forms.Textarea(attrs={'class':'address'}), 'postal_code' : forms.TextInput(attrs={'class':'postal-code'}), 'city' : forms.TextInput(attrs={'class':'city'}),
        }
