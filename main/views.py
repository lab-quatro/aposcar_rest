from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from main.permissions import \
    IsOwnerOrInRoom, IsProfileOwnerOrReadOnlyOrStaff, IsStaffOrReadOnly

from rest_framework import permissions
from rest_framework.response import Response

from main import models
from main import serializers


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [IsProfileOwnerOrReadOnlyOrStaff]

    def get_queryset(self):
        queryset = models.UserProfile.objects.all()

        ordering_query_sets = {
            'score': models.UserProfile.objects
                .annotate(score=Count('bets__is_winner')).order_by('-score'),
            '-score': models.UserProfile.objects
                .annotate(score=Count('bets__is_winner')).order_by('score'),
        }

        if ordering := self.request.query_params.get('ordering'):
            return ordering_query_sets[ordering]
        return queryset


class IndicationViewSet(viewsets.ModelViewSet):
    queryset = models.Indication.objects.all()
    serializer_class = serializers.IndicationSerializer
    permission_classes = [IsStaffOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsStaffOrReadOnly]


class NomineeViewSet(viewsets.ModelViewSet):
    queryset = models.Nominee.objects.all()
    serializer_class = serializers.NomineeSerializer
    permission_classes = [IsStaffOrReadOnly]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrInRoom]

    def get_queryset(self):
        queryset = models.Room.objects.all()

        # The user can see all rooms that he owns or belongs to.
        return queryset.filter(users__in=[self.request.user]) | \
               queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['POST'])
    def add_user(self, request, pk=None):
        room = self.get_object()
        users = models.UserProfile.objects.filter(pk__in=request.data['users'])
        for user in users:
            room.users.add(user.id)
        return Response({'status': 'new users added'})

    @action(detail=True, methods=['POST'])
    def remove_user(self, request, pk=None):
        room = self.get_object()
        users = models.UserProfile.objects.filter(pk__in=request.data['users'])
        for user in users:
            room.users.remove(user.id)
        return Response({'status': 'users removed'})

    @action(detail=True, methods=['PATCH'])
    def renew_code(self, request, pk=None):
        room = self.get_object()
        self.check_object_permissions(self.request, room)
        room.share_code = None
        room.save()
        return Response({'share_code': room.share_code})
