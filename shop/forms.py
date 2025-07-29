from django import forms

class CheckoutForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    address = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField(max_length=15)
    payment_method = forms.ChoiceField(choices=[
        ('card', 'Credit Card'),
        ('cod', 'Cash on Delivery')
    ])
