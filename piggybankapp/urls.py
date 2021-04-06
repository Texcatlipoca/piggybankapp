from django.contrib import admin
from django.urls import path
from piggybankapp.views import index, profIndex, UserView, userCollection,createUser


urlpatterns = [
    path('piggygreeting/', index, name="piggy_index"),
    path('createform/', UserView.as_view()),
    path('piggygreeting/', profIndex, name="profile_index"),
    path('api/v1/users/', userCollection, name="user_collection"),
    path('api/v1/createuser/', createUser, name="create_user")

]
