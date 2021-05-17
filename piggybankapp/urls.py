from django.contrib import admin
from django.urls import path

from piggybankapp.views import index, profIndex, UserView, userCollection
from piggybankapp.views import createUser, pigCollection, createPig, getEvents, createEvent, reminderCollection, createReminder, goalCollection, createGoal, profileCollection, createProfile, bankAccountCollection, createBankAccount, loginDetailsCollection, createLoginDetails


urlpatterns = [
    path('piggygreeting/', index, name="piggy_index"),
    path('createform/', UserView.as_view()),
    path('piggygreeting/', profIndex, name="profile_index"),
    path('api/v1/users/', userCollection, name="user_collection"),
    path('api/v1/createuser/', createUser, name="create_user"),
    path('api/v1/pigs/', pigCollection, name="pig_collection"),
    path('api/v1/createpig/', createPig, name="create_pig"),
    path('api/v1/events', getEvents, name="get_events_view"),
    path('api/v1/createEvent', createEvent, name="create_event_view"),
    path('api/v1/reminders/', reminderCollection, name='reminder_collection'),
    path('api/v1/createreminder/', createReminder, name='create_reminder'),
    path('api/v1/goals/', goalCollection, name='goal_collection'),
    path('api/v1/creategoal/', createGoal, name='create_goal'),
    path('api/v1/profiles/', profileCollection, name='profile_collection'),
    path('api/v1/createprofile/', createProfile, name='create_profile'),
    path('api/v1/bankaccount/', bankAccountCollection, name='bank_account_collection'),
    path('api/v1/createbankaccount/', createBankAccount, name='create_bank_account'),
    path('api/v1/logindetails/', loginDetailsCollection, name='login_details_collection'),
    path('api/v1/createlogindetails/', createLoginDetails, name='create_login_details')
]
