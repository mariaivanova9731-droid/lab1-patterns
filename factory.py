from abc import ABC, abstractmethod


class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):

    def send(self, message):
        print(f"Email sent: {message}")


class SMSNotification(Notification):

    def send(self, message):
        print(f"SMS sent: {message}")


class PushNotification(Notification):

    def send(self, message):
        print(f"Push notification: {message}")


class NotificationFactory:

    @staticmethod
    def create_notification(notification_type):

        if notification_type == "email":
            return EmailNotification()

        elif notification_type == "sms":
            return SMSNotification()

        elif notification_type == "push":
            return PushNotification()

        else:
            raise ValueError("Unknown notification type")


if __name__ == "__main__":

    email = NotificationFactory.create_notification("email")
    email.send("Hello by email")

    sms = NotificationFactory.create_notification("sms")
    sms.send("Hello by SMS")

    push = NotificationFactory.create_notification("push")
    push.send("Hello by push")
