from django.urls import path
from . import views

urlpatterns = [
    path('verification/', views.verification, name='verification'),
    path('signup/',views.sign_up,name="signup"),


]