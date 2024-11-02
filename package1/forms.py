from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput({'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput({'placeholder':'***********'}))

class AddUserForm(forms.Form):
    Employee_FName = forms.CharField(widget=forms.TextInput({'placeholder':'First Name'}))
    Employee_LName = forms.CharField(widget=forms.TextInput({'placeholder':'Last Name'}))
    email = forms.CharField(widget=forms.EmailInput({'placeholder':'Eg:director@thedotstechnology.tech'}))
    position = forms.CharField(widget=forms.TextInput({'placeholder':'Employee Position'}))
    salary = forms.CharField(widget=forms.NumberInput({'placeholder':'000000'}))
    password = forms.CharField(widget=forms.TextInput({'placeholder':'***********'}))