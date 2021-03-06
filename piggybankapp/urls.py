from django.contrib import admin
from django.urls import path
from .views import index, CustomerView


urlpatterns = [
    path('piggygreeting/', index, name="piggy_index"),
    path('createform/', CustomerView.as_view()),
]
