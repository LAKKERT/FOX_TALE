from django.db import models
from django.conf import settings
from datetime import date
from django.utils.timezone import now
from django.urls import reverse

# Create your models here.

User = settings.AUTH_USER_MODEL

class NewsContent(models.Model):
    introduction_content = models.TextField(max_length=158)
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Paragraph_title = models.CharField(max_length=150)
    content = models.TextField()
    date_add = models.DateField()

    def get_absolute_url(self):
        return reverse('detail_new', kwargs={'pk': self.pk})