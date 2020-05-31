from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ChatBot(models.Model):
    name = models.CharField(max_length=20, default='ChatBot')

    def __str__(self):
        return self.name


class QAForBot(models.Model):
    question = models.CharField(max_length=255, default='')
    question_slug = models.SlugField(default='')
    answer = models.CharField(max_length=255, default='')
    chatbot = models.ForeignKey(ChatBot, on_delete=models.CASCADE)


class Message(models.Model):
    text = models.CharField(max_length=255, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    author = models.CharField(max_length=255, default='')
    receiver = models.CharField(max_length=255, default='')
    time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return 'Message #' + str(self.id)
