from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        """Переопределили ready() метод конфигурации пользовательского приложения
        для выполнения задачи инициализации, которая регистрирует сигналы"""
        import accounts.signals
