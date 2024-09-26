from django.http import HttpResponse
from faker import Faker

from blog.models import Blog, Entry


def create_blog(request) -> HttpResponse:
    faker = Faker()
    saved = Entry(
        blog=[Blog(name=faker.word(), text=faker.paragraph(nb_sentences=5), author=faker.name()) for _ in range(3)],
        headline=faker.paragraph(nb_sentences=1),
    ).save()
    return HttpResponse(f"Blog created with id: {saved.id}")


def all_blogs(request) -> HttpResponse:
    blogs_timestamps = list(Entry.objects.values_list("timestamp"))

    print(blogs_timestamps)

    return HttpResponse("All blogs")
