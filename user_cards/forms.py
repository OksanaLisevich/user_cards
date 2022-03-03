from django.forms import ModelForm
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Card, CardSum


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['card_number', 'owner']


class CardSumForm(forms.ModelForm):
    class Meta:
        model = CardSum
        fields = ['card', 'sum']
