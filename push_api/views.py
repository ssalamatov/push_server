
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins

from push_api.models import Message
from push_api.serializers import MessageSerializer
from push_api.tasks import push


class MessageDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    """
        Retrieve a message instance.
        """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class MessageList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
        List all messages, or create a new.
        """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@receiver(post_save, sender=Message)
def on_create(sender, instance, **kwargs):
    start_at = instance.start_at
    pk = instance.pk
    if start_at:
        push.apply_async(args=(pk,), eta=start_at, retry=True)

    else:
        push.apply_async(args=(pk,), retry=True)


# Create your views here.
