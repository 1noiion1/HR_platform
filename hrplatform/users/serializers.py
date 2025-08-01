from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Role

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    role = serializers.ChoiceField(
        choices=Role.choices,
        default=Role.CANDIDATE,
        write_only=True
    )

    class Meta:
        model = User
        fields = ["username", "password", "role"]

    def create(self, validated_data):
        from .models import Profile
        role = validated_data.pop('role')
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        Profile.objects.create(user=user, role=role)
        return user