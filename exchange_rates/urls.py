from django.urls import path, re_path
from . import views

app_name = 'exchange_rates'

urlpatterns = [
    # path('', views.exchange_rates, name='exchange_rates'),
    path('', views.exchange_rates, name='exchange_rates'),
]
