from django.urls import path
from calculator.views import reciept

urlpatterns = [
    path('<dish>/', reciept, name='reciept'),
]
