from django.forms import ModelForm
from .models import Customer, Account, Profile

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
