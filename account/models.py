from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

'''class User(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    CHOICES = ('admin','customer')
    role = models.CharField(choices=CHOICES)'''

class ConfirmCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=4)
    valid_until = models.DateTimeField()

    def __str__(self):
        return self.code