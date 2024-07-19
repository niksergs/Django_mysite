from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token   # Импорт токена для аутентификации
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Функция приемника, которая запускается каждый раз при создании пользователя.
    Пользователь является отправителем, который несет ответственность за отправку уведомления.
    После того как метод модели пользователя save() завершил выполнение,
    он отправляет сигнал post_save в функцию-приемник create_profile,
    затем эта функция получит сигнал для создания и сохранения экземпляра профиля для этого пользователя."""
    if created:
        Profile.objects.create(user=instance)
        Token.objects.create(user=instance)     # Токен автоматически будет создаваться для пользователя
