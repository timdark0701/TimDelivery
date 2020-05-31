from django.shortcuts import render
from . import models
from django.http import HttpResponseBadRequest, JsonResponse
from django.utils import timezone

# Create your views here.


def chat(request):
    if request.user and request.user.is_authenticated:
        context = dict()
        messages = models.Message.objects.filter(user=request.user).order_by('time')
        questions = models.QAForBot.objects.all()
        context['messages'] = messages
        context['user'] = request.user
        context['joined_time'] = request.user.date_joined
        context['questions'] = questions

        return render(request, 'main/chat.html', context)
    else:
        return HttpResponseBadRequest('<h1>You have to sign in first</h1>')


def send_message(request):
    qa = models.QAForBot.objects.get(question_slug=request.GET['question_slug'])
    author = request.user.first_name
    user = request.user
    question = qa.question
    answer = qa.answer

    new_message = models.Message.objects.create(text=question, user=user, author=author, receiver='ChatBot')
    new_message.save()

    sent_message = '<div class="msg_r">\n   ' \
                   '<div class="msg">\n        ' \
                   '<p class="author_name">' + new_message.author + '<a class="msg_time">' + new_message.time.strftime('%d/%m/%y %H:%M:%S') + '</a></p>\n        ' \
                   '<p class="msg_text">' + new_message.text + '</p>\n    ' \
                   '</div>\n' \
                   '</div>'
    new_message = models.Message.objects.create(text=answer, user=user, author='ChatBot', receiver=author)
    new_message.save()

    received_message = '<div class="msg_l">\n   ' \
                   '<div class="msg">\n        ' \
                   '<p class="author_name">' + new_message.author + '<a class="msg_time">' + new_message.time.strftime('%d/%m/%y %H:%M:%S') + '</a></p>\n        ' \
                   '<p class="msg_text">' + new_message.text + '</p>\n    ' \
                   '</div>\n' \
                   '</div>'

    return JsonResponse({
        'sent_message': sent_message,
        'received_message': received_message
    })

