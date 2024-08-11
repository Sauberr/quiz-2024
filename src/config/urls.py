from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/", include("api.urls")),
    path('blog/', include('blog.urls')),
    path('quiz/', include('quiz.urls')),
]
