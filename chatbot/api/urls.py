from . import views
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'chatbot', views.ChatBotViewset)
router.register(r'qas', views.QAViewset)
router.register(r'messages', views.MessageViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('chat/', views.ChatView.as_view({'get': 'chat'}), name='chat_api'),
    path('send/', views.ChatView.as_view({'post': 'send_message'}), name='send_message_api')
]
