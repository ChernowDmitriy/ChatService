from django.db import models


class Chat(models.Model):
    """Модель чата"""
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель чата:', null=True)

    name = models.CharField(max_length=100, verbose_name='Название:')
    photo = models.ForeignKey(Files, on_delete=models.SET_NULL, verbose_name='Фото', null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
