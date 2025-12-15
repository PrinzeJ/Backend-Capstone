from .models import Booking, Menu
from django.contrib.auth.models import User

from rest_framework import serializers

class BookingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Booking
    fields = ['id', 'first_name', 'last_name', 'guest_number', 'comment']

class MenuSerializer(serializers.ModelSerializer):
  class Meta:
    model = Menu
    fields = ['id', 'name', 'price', 'description']

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'