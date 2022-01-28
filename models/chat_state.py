from django.db import models

from models.chat import Chat


class ChatState(models.Model):
    """Состоянии чата для конкретного пользователя"""

    # relations
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='Чат')

    # fields
    is_pinned = models.BooleanField(default=False, verbose_name='Закреплён?')

    def __str__(self):
        return f'{self.chat_id}'

    class Meta:
        verbose_name = 'Состоянии чата для конкретного пользователя'
        verbose_name_plural = 'Состоянии чата для конкретных пользователей'
