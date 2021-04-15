from django.urls import path

from .views import RegistrationView, ActivationView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/<str:activation_code>/', ActivationView.as_view()),
]