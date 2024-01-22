from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class SupportModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='support_author', unique=False)
    listUsers = models.ManyToManyField(User, related_name='support_list')
    reason_title = models.CharField(null=True, blank=True, max_length=150)
    problem = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('support_chat', kwargs={'pk': self.pk})

class MessageModel(models.Model):
    chat = models.ForeignKey(SupportModel, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=True, max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)