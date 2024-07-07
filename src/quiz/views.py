from .tasks import mine_bitcoin, normalize_email_task
from django.http import HttpResponse, HttpRequest


def bitcoin(request: HttpRequest) -> HttpResponse:
    mine_bitcoin.delay()
    return HttpResponse('Task is running in the background')


def normalize_email(request: HttpRequest) -> HttpResponse:
    normalize_email_task.delay(filter={'email__endswith': '.com'})
    return HttpResponse('Task is running in the background')
