from celery import shared_task

from django.core.mail import EmailMultiAlternatives


@shared_task
def send_email(subject, message, from_email, recipient_list):
    """
    Отправка электронной почты с уведомлением о заказе

    Args:
        subject: Тема письма
        message: Сообщение письма
        from_email: Адрес отправителя
        recipient_list: Список получателей
    """
    msg = EmailMultiAlternatives(subject, message, from_email, recipient_list)
    msg.send()