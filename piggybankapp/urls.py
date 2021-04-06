from django.contrib import admin
from django.urls import path
from piggybankapp.views import index, profIndex, UserView, userCollection


urlpatterns = [
    path('piggygreeting/', index, name="piggy_index"),
    path('createform/', UserView.as_view()),
    path('piggygreeting/', profIndex, name="profile_index"),
    path('api/v1/posts/', userCollection, name="user_collection")

]
