from celery import task
from django.core.mail import send_mail
from .models import Dvd

@task
def Dvd_email(dvd_id):
    order = Dvd.objects.get(id=dvd_id)
    subject = 'Your order id {}'.format(order.id)
    message = 'Dear {}. You have successfully placed an order. Your order id is {}'.format(order.user, order.id)
    Send_Mail = send_mail(subject, message, 'kennykunx@gmail.com', [kennykunx@gmail.com])
    return Send_Mail