from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from ecomerc.models import Factory, Retail, Individual
from users.models import User
from users.serializers import UserSerializer, FactorySerializer


class UserCreateAPIView(CreateAPIView):
    """ Класс создания нового пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny, )

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

        print(user.user_type.client_type)
        if user.user_type.client_type == 'FACTORY':
            Factory.objects.create(user=user)
        # elif user.user_type.client_type == 'RETAIL':      # при создании клиента, не создается предприятие...
        #     Retail.objects.create(user=user)
        # elif user.user_type.client_type == 'INDIVIDUAL':
        #     Individual.objects.create(user=user)


class UserListAPIView(ListAPIView):
    """ Класс получения всех пользователей """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny, )


class FactoryListAPIView(ListAPIView):
    """ Класс получения всех Заводов """
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = (AllowAny, )


