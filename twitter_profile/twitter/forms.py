from django import forms

from .models import Tweet, User


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

class ProfileForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100,required=False)
    last_name = forms.CharField(label='Last name', max_length=100,required=False)
    birth_date = forms.DateField(label='Birth date',required=False)
    avatar = forms.ImageField(label="Profile image",required=False)
