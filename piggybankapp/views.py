from django.shortcuts import render
from .models import Customer

def index(request):
    customer = Customer.objects.all().filter(name="Monchy").first()
    return render(request, 'index.html',{'customer': customer})
