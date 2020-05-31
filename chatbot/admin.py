from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.ChatBot)


@admin.register(models.QAForBot)
class QAAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'chatbot']
    prepopulated_fields = {'question_slug': ('question',)}


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'author', 'receiver', 'time']