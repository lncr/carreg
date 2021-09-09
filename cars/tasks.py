from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mail_to_worker(email, car_id):
    send_mail(subject='Incoming Car',
              message=f'You have received new Car request with id = {car_id}',
              recipient_list=[email, ],
              from_email=None)
