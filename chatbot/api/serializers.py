from rest_framework import serializers
from .. import models


class ChatBotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ChatBot
        fields = '__all__'


class QASerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.QAForBot
        fields = '__all__'


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Message
        fields = '__all__'

