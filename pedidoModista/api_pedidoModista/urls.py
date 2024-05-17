from django.urls import path
from .views import calcular_conversion

urlpatterns= [
    path('conversionPulgadas',calcular_conversion.as_view()),
]