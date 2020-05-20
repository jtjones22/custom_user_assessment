from django import forms


class SignUpForm(forms.Form):
    display_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class SignInForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)