from django.urls import include, path

from quiz.views import bitcoin, normalize_email, birthday_task, tuesday_noon_task, leap_year_friday_13th_task, \
    generate_choices_view, generate_quizzes_view, generate_questions_view, generate_categories_view

urlpatterns = [
    path("bitcoin/", bitcoin, name="bitcoin"),
    path("normalize_email/", normalize_email, name="normalize_email"),
    path("birthday_task/", birthday_task, name="birthday_task"),
    path("tuesday_noon_task/", tuesday_noon_task, name="tuesday_noon_task"),
    path("leap_year_friday_13th_task/", leap_year_friday_13th_task, name="leap_year_friday_13th_task"),
    path("generate_choices/", generate_choices_view, name="generate_choices"),
    path("generate_quizzes/", generate_quizzes_view, name="generate_quizzes"),
    path("generate_questions/", generate_questions_view, name="generate_questions"),
    path("generate_categories/", generate_categories_view, name="generate_categories"),
]
