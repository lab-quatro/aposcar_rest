from rest_framework import viewsets
from main import serializers
from main import models
from rest_framework import filters


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['username', 'email', 'score']


class IndicationViewSet(viewsets.ModelViewSet):
    queryset = models.Indication.objects.all()
    serializer_class = serializers.IndicationSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class NomineeViewSet(viewsets.ModelViewSet):
    queryset = models.Nominee.objects.all()
    serializer_class = serializers.NomineeSerializer
