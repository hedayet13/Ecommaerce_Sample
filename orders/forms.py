from django import forms

class CheckoutForm(forms.Form):
    email = forms.EmailField()
    shipping_address = forms.CharField(widget=forms.Textarea)
