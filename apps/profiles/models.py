from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):

    def __unicode__(self):
        return self.user.username
