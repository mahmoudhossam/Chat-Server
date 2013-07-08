from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    """Represents a message received by the server"""
    text = models.CharField(max_length=10)
    sent_by = models.ForeignKey(User)
    sent_to = models.ForeignKey(User)
    sent_at = models.DateTimeField(auto_now_add=True)
