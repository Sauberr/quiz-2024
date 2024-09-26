from django.urls import include, path

from quiz.views import bitcoin, normalize_email, birthday_task, tuesday_noon_task, leap_year_friday_13th_task

urlpatterns = [
    path("bitcoin/", bitcoin, name="bitcoin"),
    path("normalize_email/", normalize_email, name="normalize_email"),
    path("birthday_task/", birthday_task, name="birthday_task"),
    path("tuesday_noon_task/", tuesday_noon_task, name="tuesday_noon_task"),
    path("leap_year_friday_13th_task/", leap_year_friday_13th_task, name="leap_year_friday_13th_task"),
]
