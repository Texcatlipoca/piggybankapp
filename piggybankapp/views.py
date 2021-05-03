from django.shortcuts import render
from .models import User, Profile
from .forms import UserForm, ProfileForm
from django.views.generic.edit import FormView
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
<<<<<<< HEAD
from piggybankapp.models import User, Pig, Event
from piggybankapp.serializers import UserSerializer, PigSerializer, EventSerializer
=======
from piggybankapp.models import User, Pig, Reminder
from piggybankapp.serializers import UserSerializer, PigSerializer, ReminderSerializer
>>>>>>> 7737f419c76e1984cae7fda7cc126b73034e8eac
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
    

@api_view(['GET'])
def pigCollection(request):
    if request.method == 'GET':
        pigs = Pig.objects.all()
        serializer = PigSerializer(pigs, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def createPig(request):
    pig_data = JSONParser().parse(request)
    serialized_pig = PigSerializer(data=pig_data)
    if serialized_pig.is_valid():
        serialized_pig.save()
        return JsonResponse(serialized_pig.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serialized_pig.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getEvents(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def createEvent(request):
    event_data = JSONParser().parse(request)
    deserialized_event = EventSerializer(data=event_data)
    if deserialized_event.is_valid():
        deserialized_event.save()
        return JsonResponse(deserialized_event.data, status=status.HTTP_201_CREATED)
    return JsonResponse(deserialized_event.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def reminderCollection(request):
    if request.method == 'GET':
        reminders = Reminder.objects.all()
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data)



@api_view(['POST'])
def createReminder(request):
    reminder_data = JSONParser().parse(request)
    serialized_reminder = ReminderSerializer(data=reminder_data)
    if serialized_reminder.is_valid():
        serialized_reminder.save()
        return JsonResponse(serialized_reminder.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serialized_reminder.data, status=status.HTTP_400_BAD_REQUEST)