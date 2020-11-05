from rest_framework import serializers
from main import models


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Category
        fields = ['url', 'id', 'name']


class NomineeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Nominee
        fields = ['url', 'id', 'name']


class IndicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Indication
        fields = ['url', 'id', 'category', 'nominated', 'year', 'is_winner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    bets = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Indication.objects.all())

    class Meta:
        model = models.UserProfile
        fields = ['url', 'id', 'username', 'email', 'date_joined', 'profile_picture', 'score', 'bets']
