from django.contrib.auth.models import User

from .models import UzsakymoAtsiliepimas, Profilis
from django import forms

class UzsakymasReviewForm(forms.ModelForm):
    class Meta:
        model = UzsakymoAtsiliepimas
        fields = ('uzsakymas','reviewer','content')
        widgets = {'uzsakymas': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfilisUpdateForm(forms.ModelForm):
    class Meta:
        model = Profilis
        fields = ['nuotrauka']