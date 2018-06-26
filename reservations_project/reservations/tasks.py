from django.core.mail import send_mail
from reservations_project.celery import app


@app.task
def send_notification_email(email, restaurant):
    send_mail(
        'Reserve time',
        'Reminder: your reservation is in an hour. Restaurant: ' + restaurant,
        'admin@reserve.com',
        [email],
        fail_silently=False,
    )
