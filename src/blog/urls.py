from django.urls import path

from blog.views import all_blogs, create_blog

app_name = "blog"

urlpatterns = [
    path("create_blog/", create_blog, name="create_blog"),
    path("", all_blogs, name="all_blogs"),
]
