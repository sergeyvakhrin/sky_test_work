from rest_framework import serializers

from ecomerc.models import Factory
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели User """
    class Meta:
        model = User
        exclude = ('last_name', 'first_name',)


class FactorySerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Factory """
    class Meta:
        model = Factory
        fields = '__all__'
