from django.urls import path
from ecomerc.apps import EcomercConfig
from ecomerc.views import home

app_name = EcomercConfig.name

urlpatterns = [
    # path('', home, name='home'),

]
