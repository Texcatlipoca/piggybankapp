from django.forms import ModelForm
from .models import User, Account, Profile

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
