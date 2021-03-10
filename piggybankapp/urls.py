from django.contrib import admin
from django.urls import path
from .views import index, profIndex, CustomerView


urlpatterns = [
    path('piggygreeting/', index, name="piggy_index"),
    path('createform/', CustomerView.as_view()),
    path('piggygreeting/', profIndex, name="profile_index")

]
