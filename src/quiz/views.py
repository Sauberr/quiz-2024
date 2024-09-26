from django.http import HttpRequest, HttpResponse

from .tasks import mine_bitcoin, normalize_email_task, birthday_task, tuesday_noon_task, leap_year_friday_13th_task, \
    generate_choices, generate_questions, generate_quizzes, generate_categories


def bitcoin(request: HttpRequest) -> HttpResponse:
    mine_bitcoin.delay()
    return HttpResponse("Task is running in the background")


def normalize_email(request: HttpRequest) -> HttpResponse:
    normalize_email_task.delay(filter={"email__endswith": ".com"})
    return HttpResponse("Task is running in the background")


def birthday(request: HttpRequest) -> HttpResponse:
    birthday_task.delay()
    return HttpResponse("Task is running in the background")


def tuesday_noon(request: HttpRequest) -> HttpResponse:
    tuesday_noon_task.delay()
    return HttpResponse("Task is running in the background")


def leap_year_friday_13th(request: HttpRequest) -> HttpResponse:
    leap_year_friday_13th_task.delay()
    return HttpResponse("Task is running in the background")


def generate_categories_view(request: HttpRequest) -> HttpResponse:
    generate_categories.delay()
    return HttpResponse("Task is running in the background")


def generate_quizzes_view(request: HttpRequest) -> HttpResponse:
    generate_quizzes.delay()
    return HttpResponse("Task is running in the background")


def generate_questions_view(request: HttpRequest) -> HttpResponse:
    generate_questions.delay()
    return HttpResponse("Task is running in the background")


def generate_choices_view(request: HttpRequest) -> HttpResponse:
    generate_choices.delay()
    return HttpResponse("Task is running in the background")