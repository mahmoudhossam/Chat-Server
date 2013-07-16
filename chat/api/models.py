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


class Buddies(models.Manager):

    def already_added(self, user, buddy):
        buddylist = self.objects.get(user=user)
        return buddylist.objects.filter(buddy=buddy)

    def add_buddy(self, user, username):
        try:
            buddy = User.objects.get(username=username)
            if already_added(user, buddy):
                return
            buddylist = BuddyList(user, buddy)
            buddylist.save()
            return True
        except DoesNotExist:
            return False

    def get_user_buddies(self, user):
        return self.objects.filter(user=user)


class BuddyList(models.Model):
    """represents a user's buddy list"""
    user = models.OneToOneField(User)
    buddy = models.ForeignKey(User, related_name='buddy')

    objects = models.Manager()
    buddies = Buddies()
