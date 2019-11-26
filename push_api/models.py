from django.db import models


Viber = 0
Telegram = 1
WhatsApp = 2


MESSAGE_NOT_SENT = 0
MESSAGE_OK = 1


class Message(models.Model):
    user_id = models.CharField(max_length=200)
    messenger_id = models.IntegerField(blank=False, choices=(
        (Viber, 'Viber'),
        (Telegram, 'Telegram'),
        (WhatsApp, 'WhatsApp'),
    ))
    text = models.TextField()
    created = models.DateTimeField('time of create', auto_now_add=True)
    start_at = models.DateTimeField('time of start', blank=True, null=True)
    message_status = models.IntegerField(default=0, blank=True, choices=(
        (MESSAGE_NOT_SENT, 'Not sent'),
        (MESSAGE_OK, 'OK'),
    ))

    def message_is_send(self):
        if self.message_status == 0:
            self.message_status = 1
            self.save()

    def __str__(self):
        return '%s' % self.__dict__

    class Meta:
        ordering = ['id']

# Create your models here.
