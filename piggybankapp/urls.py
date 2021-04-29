from django.contrib import admin
from django.urls import path
from piggybankapp.views import index, profIndex, UserView, userCollection,createUser, pigCollection, createPig


urlpatterns = [
    path('piggygreeting/', index, name="piggy_index"),
    path('createform/', UserView.as_view()),
    path('piggygreeting/', profIndex, name="profile_index"),
    path('api/v1/users/', userCollection, name="user_collection"),
    path('api/v1/createuser/', createUser, name="create_user"),
    path('api/v1/pigs/', pigCollection, name="pig_collection"),
    path('api/v1/createpig/', createPig, name="create_pig")
 
]
