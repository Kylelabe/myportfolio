# forms.py
from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Michael Jordan', 'class': 'form-control'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'michael.j@gmail.com', 'class': 'form-control'}))
    subject = forms.CharField(max_length=100,
                              widget=forms.TextInput(attrs={'placeholder': 'Say hi to you', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Here you can write your nice text', 'class': 'form-control', 'rows': 8}))
