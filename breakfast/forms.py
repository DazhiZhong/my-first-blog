from django import forms

from .models import breakfastho

class  breakfast_form(forms.Form):
    Name = forms.CharField()
    Description = forms.CharField(label='Despacito', widget=forms.Textarea(attrs={
        'rows': 10,
        'cols': 20,
        'placeholder':'this is so shitty I just can\'t', 
    }))
    Price = forms.DecimalField()



class breakfast_form_new(forms.ModelForm):
    Price = forms.DecimalField(initial=399.99)

    class Meta:
        model = breakfastho
        fields = [
            'Name',
            'Description',
            'Price'
        ]