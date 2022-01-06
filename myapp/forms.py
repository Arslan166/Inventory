from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myapp.models import Customer, shop
#form about order
class Customerform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']



class OrderForm(forms.ModelForm):
    class Meta:
        model = shop
        fields = '__all__'

class createuserform(UserCreationForm):
        class Meta:
            model = User
            fields = ['username','email','password1','password2']