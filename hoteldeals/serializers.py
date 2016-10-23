from django.contrib.auth.models import User
from rest_framework import serializers
from hoteldeals.models import Deals


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class DealsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deals
        fields = ('name', 'image', 'rating', 'link', 'actual_price', 'discount', 'location')


class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deals
        fields = ('name', 'image', 'rating', 'link', 'actual_price', 'discount', 'location')


class StatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deals
        fields = ('rating',)
