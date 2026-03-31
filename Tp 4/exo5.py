class EmailService:
    def send_email(self, message):
        pass
class UserNotification:
    def __init__(self):
        self.email_service = EmailService() # Tight coupling!
    def notify(self, user, message):
        self.email_service.send_email(message)

# DIP = Dependency Inversion Principle
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def notify(self, user, message): pass

class EmailService(NotificationService):
    def notify(self, user, message):
        print(f"Email to {user}: {message}")

class UserNotification:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def notify(self, user, message):
        self.notification_service.notify(user, message)


