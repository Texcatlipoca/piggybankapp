from django.shortcuts import render
from .models import User, Profile
from .forms import UserForm, ProfileForm
from django.views.generic.edit import FormView

def index(request):
    user = User.objects.all().filter(name="Monchy").first()
    return render(request, 'index.html',{'user': user})

def profIndex(request):
    profile = Profile.objects.all().filter(username="Porky").first()
    return render(request, 'profindex.html',{'profile': profile})



class UserView(FormView):
    template_name = 'index.html'
    form_class = UserForm

    def form_valid(self, form):
        print('data before saving')
        print(form.cleaned_data)
        form.save()
        saved_user = User.objects.all().filter(name='abc')[0]
        print('customer after saving')
        print(saved_user)


        return super().form_valid(form)

    success_url ="/piggy/createform/"


