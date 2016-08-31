from django import forms

from .models import Tweet, User


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

class ProfileForm(forms.Form):
    
    username = forms.CharField(label='Username', max_length=100,required=False,disabled=True)
    first_name = forms.CharField(label='First name', max_length=100,required=False)
    last_name = forms.CharField(label='Last name', max_length=100,required=False)
    birth_date = forms.DateField(label='Birth date',required=False) #, input_formats='%Y-%m-%d'
    #comment = forms.CharField(widget=forms.Textarea)
    avatar = forms.ImageField(widget=forms.ClearableFileInput, label="Profile image:",required=False)

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name',
#                     'birth_date', 'avatar']
