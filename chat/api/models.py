from django.db import models
from django.contrib.auth.models import User


class Messages(models.Manager):

    def sent_by(self, user):
        return self.objects.filter(sender=user)


class Message(models.Model):
    """Represents a message received by the server"""
    text = models.CharField(max_length=10)
    sender = models.ForeignKey(User, related_name='message_sender')
    recipient = models.ForeignKey(User, related_name='message_recipient')

    objects = models.Manager()
    messages = Messages()
