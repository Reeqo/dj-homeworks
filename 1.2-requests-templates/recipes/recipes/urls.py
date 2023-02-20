from django.urls import path
from calculator.views import reciept

urlpatterns = [
    path('index.html/<dish>/<servings>', reciept, name='reciept'),
]
