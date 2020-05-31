from . import serializers
from .. import models
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from main.context_processor_api import common_context
from django.shortcuts import redirect


class ChatBotViewset(viewsets.ModelViewSet):
    queryset = models.ChatBot.objects.all()
    serializer_class = serializers.ChatBotSerializer
    http_method_names = ['get']


class QAViewset(viewsets.ModelViewSet):
    queryset = models.QAForBot.objects.all()
    serializer_class = serializers.QASerializer
    http_method_names = ['get']


class MessageViewset(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = [permissions.IsAdminUser]


class ChatView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def chat(self, request):
        data = dict()
        messages = models.Message.objects.filter(user=request.user).order_by('time')
        questions = models.QAForBot.objects.all()
        data['messages'] = serializers.MessageSerializer(messages, many=True, context={'request': request}).data
        data['joined_time'] = request.user.date_joined
        data['questions'] = serializers.QASerializer(questions, many=True, context={'request': request}).data
        data.update(common_context(request))
        return Response(data)

    def send_message(self, request):
        qa = models.QAForBot.objects.get(question_slug=request.data['question_slug'])
        author = request.user.first_name
        user = request.user
        question = qa.question
        answer = qa.answer

        sent_msg = models.Message.objects.create(text=question, user=user, author=author, receiver='ChatBot')
        sent_msg.save()

        received_msg = models.Message.objects.create(text=answer, user=user, author='ChatBot', receiver=author)
        received_msg.save()

        return redirect('chat_api')

