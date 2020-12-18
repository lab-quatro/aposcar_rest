from rest_framework import serializers
from main import models


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Category
        fields = ['url', 'id', 'name']


class NomineeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Nominee
        fields = ['url', 'id', 'name', 'picture_url', 'description']


class IndicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Indication
        fields = ['url', 'id', 'category', 'nominated',
                  'year', 'is_winner', 'annotation']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    bets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=models.Indication.objects.all(), required=False
    )
    score = serializers.SerializerMethodField()

    class Meta:
        model = models.UserProfile
        fields = ['url', 'id', 'username', 'email', 'date_joined',
                  'profile_picture', 'bets', 'score', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'date_joined': {'read_only': True}
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        instance.set_password(password)
        return super().update(instance, validated_data)

    def get_score(self, obj):
        return obj.bets.filter(is_winner=True).count()

    def validate_bets(self, value):
        categories = [indication.category for indication in value]

        # Convert to set to remove the duplicates,
        # and check if the list len is still the same
        if len(categories) != len(set(categories)):
            raise serializers.ValidationError(
                "You can't place two bets to the same category!"
            )
        return value


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='userprofile-detail'
    )

    class Meta:
        model = models.Room
        fields = ['url', 'id', 'name', 'owner', 'users', 'share_code']


class IndicationReadOnlySerializer(IndicationSerializer):
    # This serializer is provided by convenience and is used in
    # the retrieve and list actions of the Indications view
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    nominated = NomineeSerializer(read_only=True)

    class Meta:
        model = models.Indication
        fields = IndicationSerializer.Meta.fields
