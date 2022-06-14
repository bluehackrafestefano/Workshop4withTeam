from .models import Pizza
from django import forms

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)