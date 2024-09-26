import random
import time
from django.utils import timezone

from celery import shared_task
from django.contrib.auth import get_user_model


@shared_task
def mine_bitcoin():
    time.sleep(random.randint(1, 10))


@shared_task
def normalize_email_task(filter):
    users = get_user_model().objects.filter(**filter)
    if users:
        for user in users:
            print(f"Working with user: {user.email}")
            user.save()
    else:
        print("Empty query set!")

    return f"Normalized emails for {len(users)} users."


@shared_task
def birthday_task():
    User = get_user_model()
    now = timezone.now()

    users = User.objects.all()
    for user in users:
        if user.birth_data:
            birth_date_this_year = user.birth_date.replace(year=now.year)
            if now.date() == birth_date_this_year:
                print(f'Happy birthday, {user.username}!')


@shared_task
def tuesday_noon_task():
    if timezone.now().weekday() == 1 and timezone.now().hour() == 12:
        print("It's Tuesday")


@shared_task
def leap_year_friday_13th_task():
    now = timezone.now()
    if now.year() % 4 == 0 and now.weekday() == 4 and now.day() == 13:
        print("It's Friday 13th in a leap year")
