from django.contrib.auth.models import User


def create_user(username, email, password):
    User.objects.create_user(username, email, password)
