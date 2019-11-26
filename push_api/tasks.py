import celery

from django.conf import settings
from push_api import clients
from push_api.models import Message


CELERY_NUMBER_RETRIES = getattr(settings, 'CELERY_NUMBER_RETRIES')


def get_client_messenger(messenger_id):
    if messenger_id == 0:
        return clients.ViberClient()
    elif messenger_id == 1:
        return clients.TelegramClient()
    else:
        return clients.WhatsAppClient()


@celery.shared_task(bind=True, max_retries=CELERY_NUMBER_RETRIES)
def push(self, pk):
    """ task for sending messages, if error occurs, retry for 5 sec """
    message = Message.objects.get(pk=pk)
    client = get_client_messenger(message.messenger_id)
    try:
        client.push(message.user_id, message.text)
    except Exception:
        self.retry(countdown=5)
    message.message_is_send()
