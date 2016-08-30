from django import forms

from .models import Tweet, User


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']


class ProfileForm(forms.Form):
    avatar = forms.ImageField(required=False)
    username = forms.CharField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    birth_date = forms.DateField(required=False)
