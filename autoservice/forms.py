from .models import UzsakymoAtsiliepimas
from django import forms

class UzsakymasReviewForm(forms.ModelForm):
    class Meta:
        model = UzsakymoAtsiliepimas
        fields = ('uzsakymas','reviewer','content')
        widgets = {'uzsakymas': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}