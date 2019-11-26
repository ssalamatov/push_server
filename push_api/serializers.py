from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from push_api.models import Message


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'user_id', 'messenger_id', 'text', 'start_at']

        validators = [
            UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=['user_id', 'messenger_id', 'text']
            )
        ]
