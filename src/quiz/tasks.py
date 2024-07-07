import time
import random

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
            print(f'Working with user: {user.email}')
            user.save()
    else:
        print('Empty query set!')

    return f'Normalized emails for {len(users)} users.'
