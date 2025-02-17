"""
Serializers for the user API view.
"""

from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = { 'password': {'write_only': True, 'min_length': 5}}

    # Override the create method that the serializer uses automatically to
    # create a new object and use the create_user method from the model itself

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)