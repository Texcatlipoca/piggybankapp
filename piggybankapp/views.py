from django.shortcuts import render
from .models import User, Profile
from .forms import UserForm, ProfileForm
from django.views.generic.edit import FormView
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from piggybankapp.models import User
from piggybankapp.serializers import UserSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse


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
        form.save()
        saved_user = User.objects.all().filter(name='abc')[0]

        return super().form_valid(form)

    success_url ="/piggy/createform/"


@api_view(['GET'])
def userCollection(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    user_data = JSONParser().parse(request)
    serialized_user = UserSerializer(data=user_data)
    if serialized_user.is_valid():
        serialized_user.save()
        return JsonResponse(serialized_user.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serialized_user.data, status=status.HTTP_400_BAD_REQUEST)
    