from rest_framework import serializers
from .models import UserQuerries


class UserQuerriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserQuerries
        fields = '__all__'
