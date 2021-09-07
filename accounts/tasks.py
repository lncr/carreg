from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mail_to_worker(user, car):
    send_mail(subject='New Car',
              from_email=None,
              message=f'You have received a car to work on. {car.id}',
              recipient_list=[user.email, ])
