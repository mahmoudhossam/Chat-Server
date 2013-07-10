from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    """Represents a message received by the server"""
    text = models.CharField(max_length=10)
    sender = models.ForeignKey(User, related_name='message_sender')
    recipient = models.ForeignKey(User, related_name='message_recipient')
