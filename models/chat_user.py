from django.db import models

from models.chat import Chat


class ChatUser(models.Model):
    """Пользователь чата"""

    # relations
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='Чат')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True)

    # fields
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания чата:')
    is_delete = models.BooleanField(default=False)
    is_left = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.chat_id}'

    class Meta:
        verbose_name = 'Пользователь чатов'
        verbose_name_plural = 'Пользователи чатов'
