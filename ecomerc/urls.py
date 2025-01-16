from django.urls import path
from ecomerc.apps import EcomercConfig
from ecomerc.views import home

app_mame = EcomercConfig.name

urlpatterns = [
    path('', home, name='home'),

]
