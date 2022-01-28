from django.db import models

from models.chat import Chat


class ChatMessage(models.Model):
    """Модель для сообщения из чата"""

    # relations
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='Чат')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Автор', null=True)
    # Добавить m2m связка, таблица будет называться message_state

    # fields
    text = models.TextField(verbose_name='Текст')
    reply_id = models.IntegerField(verbose_name='ID сообщение на которое ответили', null=True, blank=True)
    is_delete = models.BooleanField(default=False, verbose_name='Удалено?')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания сообщения')
    updated_at = models.DateTimeField(auto_now_add=False, verbose_name='Дата обновления сообщения', blank=True,
                                      null=True)
    deleted_at = models.DateTimeField(auto_now_add=False, verbose_name='Дата удаления сообщения', blank=True,
                                      null=True)

    class Meta:
        verbose_name = 'Сообщение из чата'
        verbose_name_plural = 'Сообщения из чатов'
