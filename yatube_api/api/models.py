from django.contrib.auth import get_user_model
from django.db import models


MAX_LEN = 256

User = get_user_model()


class Group(models.Model):
    title = models.CharField('Заголовок', max_length=MAX_LEN)
    slug = models.SlugField(
        'Идентификатор группы',
        unique=True,
        help_text='Идентификатор группы; разрешены '
        'символы латиницы, цифры, дефис и подчёркивание.'
    )
    description = models.TextField('Описание группы')

    def __str__(self):
        return self.title


# class Follow(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='followings')
#     following = models.ManyToManyField(
#         'self',
#         verbose_name='Подписки',
#         related_name='followers',
#         symmetrical=False
#     )
