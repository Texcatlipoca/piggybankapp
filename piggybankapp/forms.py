from django.forms import ModelForm
from .models import User, Account, Profile, Reminder, Pig, Event, Goal

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

class ReminderForm(ModelForm):
    class Meta:
        model = Reminder
        fields = '__all__'

class Pigform(ModelForm):
    class Meta:
        model = Pig
        fields = '__all__'

class Eventform(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class Goalform(ModelForm):
    class Meta:
        model = Goal
        fields = '__all__'
